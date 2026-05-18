# -*- coding: utf-8 -*-
import os
import time
import random
import threading

from flask import Flask, jsonify, send_from_directory, Response
from flask_socketio import SocketIO, emit

from config import (
    AKAMAI_RANGES, FASTLY_RANGES, OPERATORS,
    DEFAULT_PORTS, DEFAULT_THREADS, DEFAULT_TIMEOUT,
    MAX_THREADS, SERVER_PORT, TELEGRAM_ENABLED
)
from utils import parse_ip_input, unique_ips
from engine import Scanner
from saver import save_results, list_files
from page import HTML
import telegram_bot

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ipscannerkey'
socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    async_mode='threading',
    ping_timeout=120,
    ping_interval=25,
)

engine = Scanner()


@app.route('/')
def index():
    return Response(HTML, content_type='text/html; charset=utf-8')


@app.route('/api/ranges')
def api_ranges():
    return jsonify({'akamai': AKAMAI_RANGES, 'fastly': FASTLY_RANGES})


@app.route('/api/operators')
def api_operators():
    ops = {}
    for key, val in OPERATORS.items():
        ops[key] = val['name']
    return jsonify(ops)


@app.route('/api/files')
def api_files():
    return jsonify(list_files())


@app.route('/api/download/<path:fn>')
def api_download(fn):
    return send_from_directory(
        os.path.abspath('results'), fn, as_attachment=True
    )


@socketio.on('connect')
def on_connect():
    print("[+] Client connected")


@socketio.on('start_scan')
def on_start(data):
    print("[*] start_scan mode:", data.get('mode'))

    if engine.running:
        engine.stop()
        time.sleep(0.3)

    m = data.get('mode', 'custom')
    ipt = data.get('ips', '')
    pts = data.get('ports', '443,80')
    thr = min(int(data.get('threads', DEFAULT_THREADS)), MAX_THREADS)
    tout = float(data.get('timeout', DEFAULT_TIMEOUT))
    samp = int(data.get('sample', 500))
    do_http = bool(data.get('do_http', False))
    sel = data.get('selected_ranges', [])
    operator = data.get('operator', 'none')

    ports = []
    for p in pts.split(','):
        p = p.strip()
        if p.isdigit():
            ports.append(int(p))
    if not ports:
        ports = DEFAULT_PORTS[:]

    ips = []
    if m in ('akamai', 'fastly', 'both'):
        rng = sel if sel else []
        if not rng:
            if m == 'akamai':
                rng = AKAMAI_RANGES
            elif m == 'fastly':
                rng = FASTLY_RANGES
            else:
                rng = AKAMAI_RANGES + FASTLY_RANGES
        all_ips = []
        for r in rng:
            all_ips.extend(parse_ip_input(r))
        if len(all_ips) > samp:
            ips = random.sample(all_ips, samp)
        else:
            ips = all_ips
    else:
        for line in ipt.strip().split('\n'):
            line = line.strip()
            if line and not line.startswith('#'):
                ips.extend(parse_ip_input(line))

    ips = unique_ips(ips)

    if not ips:
        emit('scan_error', {'message': 'No valid IPs found!'})
        return

    print("[*] {} IPs | {} threads | timeout {}s | http={}".format(
        len(ips), thr, tout, do_http))

    def run():
        engine.start(ips, ports, thr, tout, do_http, socketio)

    threading.Thread(target=run, daemon=True).start()


@socketio.on('stop_scan')
def on_stop():
    print("[*] Stop received")
    engine.stop()
    emit('scan_stopped', {})


@socketio.on('save_results')
def on_save(data):
    if not engine.results:
        emit('save_error', {'message': 'No results to save!'})
        return
    fmt = data.get('format', 'txt')
    try:
        fn, cn = save_results(list(engine.results), fmt)
        emit('save_ok', {
            'filename': fn,
            'clean_filename': cn,
            'count': len(engine.results),
        })
    except Exception as e:
        emit('save_error', {'message': str(e)})


@socketio.on('send_telegram')
def on_send_telegram(data):
    if not engine.results:
        emit('telegram_error', {'message': 'No results to send!'})
        return

    tg_token = data.get('tg_token', '').strip()
    tg_channel = data.get('tg_channel', '').strip()
    operator = data.get('operator', 'none')

    if not tg_token or not tg_channel:
        emit('telegram_error', {'message': 'Enter Bot Token and Channel ID!'})
        return

    operator_name = ""
    if operator in OPERATORS:
        operator_name = OPERATORS[operator]['name']

    print("[*] Sending to Telegram: {} IPs, op={}".format(
        len(engine.results), operator_name))

    def do_send():
        try:
            ok = telegram_bot.send_scan_complete(
                tg_token,
                tg_channel,
                engine.scanned,
                len(engine.results),
                engine.results,
                operator_name
            )
            if ok:
                socketio.emit('telegram_ok', {
                    'count': len(engine.results)
                }, namespace='/')
                print("[+] Telegram sent!")
            else:
                socketio.emit('telegram_error', {
                    'message': 'Failed to send'
                }, namespace='/')
        except Exception as e:
            print("[-] Telegram error:", e)
            socketio.emit('telegram_error', {
                'message': str(e)
            }, namespace='/')

    threading.Thread(target=do_send, daemon=True).start()


if __name__ == '__main__':
    os.makedirs('results', exist_ok=True)
    print("")
    print("=" * 40)
    print("  IP Scanner - @Net4All_None")
    print("  http://127.0.0.1:{}".format(SERVER_PORT))
    print("=" * 40)
    print("")
    socketio.run(
        app,
        host='0.0.0.0',
        port=SERVER_PORT,
        debug=False,
        allow_unsafe_werkzeug=True,
            )
