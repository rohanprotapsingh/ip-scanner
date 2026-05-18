# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json
import time as _time


def send_message(bot_token, chat_id, text):
    if not bot_token or not chat_id:
        return False
    try:
        thread_id = None
        target_chat_id = chat_id
        if ":" in str(chat_id):
            parts = str(chat_id).split(":")
            target_chat_id = parts[0]
            thread_id = parts[1]
        url = "https://api.telegram.org/bot{}/sendMessage".format(bot_token)
        payload = {
            'chat_id': target_chat_id,
            'text': text,
            'parse_mode': 'HTML',
            'disable_web_page_preview': True
        }
        if thread_id:
            payload['message_thread_id'] = thread_id
        data = urllib.parse.urlencode(payload).encode('utf-8')
        req = urllib.request.Request(url, data=data)
        with urllib.request.urlopen(req, timeout=15) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            if res_data.get('ok'):
                print("[+] Telegram: sent!")
                return True
            else:
                print("[-] Telegram:", res_data)
                return False
    except Exception as e:
        print("[-] Telegram:", str(e))
        return False


def send_scan_complete(bot_token, chat_id, total_scanned, total_found, all_ips, operator_name=""):
    medals = ["1", "2", "3"]
    top3 = all_ips[:3]

    header = []
    header.append("IP Scan Complete")
    header.append("")
    if operator_name:
        header.append("Operator: {}".format(operator_name))
        header.append("")
    header.append("Results:")
    header.append("Scanned: {}".format(total_scanned))
    header.append("Found: {}".format(total_found))
    header.append("")
    header.append("Top 3 Fastest IPs:")
    header.append("")
    for i, ip in enumerate(top3):
        header.append("{}. {}".format(medals[i], ip['ip']))

    ip_lines = []
    for ip in all_ips:
        ip_lines.append(ip['ip'])
    ip_block = "\n".join(ip_lines)

    full = list(header)
    full.append("")
    full.append("")
    full.append("Full IP List:")
    full.append("")
    full.append("<code>{}</code>".format(ip_block))
    full.append("")
    full.append("Copy all IPs above")
    full.append("")
    full.append("Tutorial:")
    full.append("")
    full.append("1. Remove old app and install new version")
    full.append("")
    full.append("2. Go to More Options")
    full.append("")
    full.append("3. Enable Beast Mode")
    full.append("")
    full.append("4. Select CDN Fronting from Connection Protocol")
    full.append("")
    full.append("5. Paste IPs in CDN edge IPs section")
    full.append("")
    full.append("6. Start and wait to connect")
    full.append("")
    full.append("@Net4All_none")

    full_msg = '\n'.join(full)

    if len(full_msg) <= 4000:
        return send_message(bot_token, chat_id, full_msg)

    send_message(bot_token, chat_id, '\n'.join(header) + "\n\n@Net4All_none")

    chunk_size = 50
    for i in range(0, len(all_ips), chunk_size):
        chunk = all_ips[i:i + chunk_size]
        idx = i // chunk_size + 1
        total_chunks = (len(all_ips) + chunk_size - 1) // chunk_size
        is_last = (idx == total_chunks)

        msg = []
        msg.append("IP List ({}/{}):".format(idx, total_chunks))
        msg.append("")
        msg.append("<code>{}</code>".format(
            '\n'.join([ip['ip'] for ip in chunk])
        ))

        if is_last:
            msg.append("")
            msg.append("Copy all IPs above")
            msg.append("")
            msg.append("Tutorial:")
            msg.append("")
            msg.append("1. Remove old app and install new version")
            msg.append("2. Go to More Options")
            msg.append("3. Enable Beast Mode")
            msg.append("4. Select CDN Fronting")
            msg.append("5. Paste IPs in CDN edge IPs")
            msg.append("6. Start and wait")
            msg.append("")
            msg.append("@Net4All_none")

        send_message(bot_token, chat_id, '\n'.join(msg))
        _time.sleep(1)

    return True
