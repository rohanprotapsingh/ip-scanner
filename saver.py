# -*- coding: utf-8 -*-
import os
import csv
import json
from datetime import datetime

RESULTS_DIR = "results"


def ensure_dir():
    os.makedirs(RESULTS_DIR, exist_ok=True)


def save_results(results, fmt):
    ensure_dir()
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    fname = "scan_{}.{}".format(ts, fmt)
    fpath = os.path.join(RESULTS_DIR, fname)
    data = sorted(results, key=lambda x: x['latency_ms'])
    if fmt == "txt":
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write("# Scan Results - {}\n# Total: {}\n\n".format(
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'), len(data)))
            for i, r in enumerate(data, 1):
                f.write("{:4d} | {:>15s}:{:<5d} | {:>8.1f}ms | {:<12s} | HTTP {} | {}\n".format(
                    i, r['ip'], r['port'], r['latency_ms'],
                    r['provider'], r['http_status'], r['server_header']))
    elif fmt == "csv":
        with open(fpath, 'w', newline='', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerow(['Rank','IP','Port','Latency_ms','Provider','HTTP','TLS','Server'])
            for i, r in enumerate(data, 1):
                w.writerow([i, r['ip'], r['port'], r['latency_ms'],
                    r['provider'], r['http_status'], r['tls_valid'], r['server_header']])
    elif fmt == "json":
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump({"scan_time": datetime.now().isoformat(), "total": len(data),
                "results": [dict(rank=i, **r) for i, r in enumerate(data, 1)]
            }, f, indent=2, ensure_ascii=False)
    cn = "scan_{}_clean.txt".format(ts)
    cp = os.path.join(RESULTS_DIR, cn)
    with open(cp, 'w', encoding='utf-8') as f:
        for r in data:
            f.write(r['ip'] + '\n')
    return fname, cn


def list_files():
    ensure_dir()
    files = []
    for f in sorted(os.listdir(RESULTS_DIR), reverse=True):
        fp = os.path.join(RESULTS_DIR, f)
        if os.path.isfile(fp):
            files.append({'name': f, 'size': os.path.getsize(fp)})
    return files
