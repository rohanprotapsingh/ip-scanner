# -*- coding: utf-8 -*-
import socket
import ssl
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock, Event
from utils import detect_cdn


class Scanner:
    def __init__(self):
        self.results = []
        self.scanned = 0
        self.total = 0
        self.running = False
        self.lock = Lock()
        self.stop_event = Event()

    def reset(self):
        self.results = []
        self.scanned = 0
        self.stop_event.clear()

    def tcp_ping(self, ip, port, timeout):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            t0 = time.perf_counter()
            err = s.connect_ex((ip, port))
            ms = round((time.perf_counter() - t0) * 1000, 1)
            s.close()
            if err == 0:
                return ms
        except Exception:
            pass
        return None

    def http_head(self, ip, port, timeout):
        scheme = "https" if port == 443 else "http"
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            req = urllib.request.Request(
                "{}://{}:{}/".format(scheme, ip, port),
                method='HEAD',
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            if port == 443:
                h = urllib.request.HTTPSHandler(context=ctx)
            else:
                h = urllib.request.HTTPHandler()
            opener = urllib.request.build_opener(h)
            t0 = time.perf_counter()
            resp = opener.open(req, timeout=timeout)
            ms = round((time.perf_counter() - t0) * 1000, 1)
            return ms, resp.status, resp.headers.get('Server', '')
        except Exception:
            return None, 0, ''

    def scan_one(self, ip, ports, timeout, do_http, sio):
        if self.stop_event.is_set():
            return
        best = None
        for port in ports:
            if self.stop_event.is_set():
                return
            ms = self.tcp_ping(ip, port, timeout)
            if ms is None:
                continue
            srv = ''
            hst = 0
            if do_http and not self.stop_event.is_set():
                hms, hst, srv = self.http_head(ip, port, min(timeout, 2))
                if hms is not None:
                    ms = hms
            cdn = detect_cdn(srv)
            r = {
                'ip': ip, 'port': port, 'latency_ms': ms,
                'provider': cdn, 'http_status': hst,
                'tls_valid': port == 443 and hst > 0,
                'server_header': srv,
            }
            if best is None or ms < best['latency_ms']:
                best = r

        if self.stop_event.is_set():
            return

        with self.lock:
            self.scanned += 1
            sc = self.scanned
            cnt = len(self.results)
            if best:
                self.results.append(best)
                cnt += 1

        if best and sio:
            try:
                sio.emit('ip_found', best, namespace='/')
            except Exception:
                pass
        if sio and not self.stop_event.is_set():
            pct = round((sc / self.total) * 100, 1) if self.total > 0 else 0
            try:
                sio.emit('scan_progress', {
                    'scanned': sc, 'total': self.total,
                    'found': cnt, 'percent': pct,
                }, namespace='/')
            except Exception:
                pass

    def start(self, ips, ports, threads, timeout, do_http, sio):
        self.reset()
        self.total = len(ips)
        self.running = True
        if sio:
            try:
                sio.emit('scan_started', {'total': self.total}, namespace='/')
            except Exception:
                pass
        with ThreadPoolExecutor(max_workers=threads) as pool:
            futs = []
            for ip in ips:
                if self.stop_event.is_set():
                    break
                futs.append(pool.submit(self.scan_one, ip, ports, timeout, do_http, sio))
            for f in as_completed(futs):
                if self.stop_event.is_set():
                    for fut in futs:
                        fut.cancel()
                    break
                try:
                    f.result()
                except Exception:
                    pass
        self.results.sort(key=lambda x: x['latency_ms'])
        self.running = False
        if self.stop_event.is_set():
            if sio:
                try:
                    sio.emit('scan_stopped', {}, namespace='/')
                except Exception:
                    pass
            return
        if sio:
            try:
                sio.emit('scan_progress', {
                    'scanned': self.scanned, 'total': self.total,
                    'found': len(self.results), 'percent': 100,
                }, namespace='/')
                sio.emit('scan_complete', {
                    'total_scanned': self.scanned,
                    'total_found': len(self.results),
                    'results': self.results[:2000],
                }, namespace='/')
            except Exception:
                pass

    def stop(self):
        self.stop_event.set()
        self.running = False
