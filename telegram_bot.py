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


def build_message(total_scanned, total_found, all_ips, operator_name=""):
    top3 = all_ips[:3]
    medals = ["\U0001f947", "\U0001f948", "\U0001f949"]

    ip_list = "\n".join([ip['ip'] for ip in all_ips])

    lines = []
    lines.append("\U0001f50d IP Scan Complete")
    lines.append("")
    lines.append("")
    if operator_name:
        lines.append("\U0001f4f6 Operator: {}".format(operator_name))
        lines.append("")
    lines.append("\U0001f4ca Results:")
    lines.append("\u2022 Scanned: {}".format(total_scanned))
    lines.append("\u2022 Found: {}".format(total_found))
    lines.append("")
    lines.append("\U0001f3c6 Top 3 Fastest IPs:")
    lines.append("")
    for i, ip in enumerate(top3):
        lines.append("{} {}".format(medals[i], ip['ip']))
    lines.append("")
    lines.append("")
    lines.append("\u2728 \u0644\u06cc\u0633\u062a \u06a9\u0627\u0645\u0644 \u0622\u06cc\u200c\u067e\u06cc :")
    lines.append("")
    lines.append("<blockquote expandable><code>{}</code></blockquote>".format(ip_list))
    lines.append("")
    lines.append("\u2b05\ufe0f \u0647\u0645\u0631\u0648 \u0628\u0627 \u0647\u0645 \u0648\u0627\u0631\u062f \u06a9\u0646\u06cc\u062f \U0001f4f0")
    lines.append("")
    lines.append("\u270f \u0622\u0645\u0648\u0632\u0634 \u0645\u062a\u0646\u06cc :")
    lines.append("")
    lines.append("1\u20e3 \u0646\u0633\u062e\u0647 \u0634\u06cc\u0631 \u062e\u0648\u0631\u0634\u06cc\u062f \u0627\u06af\u0647 \u0627\u0632 \u0642\u0628\u0644 \u062f\u0627\u0631\u06cc\u062f \u062d\u0630\u0641 \u06a9\u0646\u06cc\u062f \u0648 \u0646\u0633\u062e\u0647 \u062c\u062f\u06cc\u062f \u0646\u0635\u0628 \u06a9\u0646\u06cc\u062f")
    lines.append("")
    lines.append("2\u20e3 \u06af\u0627\u0645 \u062f\u0648\u0645 \u0628\u0631\u06cc\u062f \u0642\u0633\u0645\u062a More Options \u06cc\u0627 \u0627\u06af\u0647 \u0632\u0628\u0627\u0646 \u0641\u0627\u0631\u0633\u06cc \u0647\u0633\u062a\u06cc\u062f \u0628\u0631\u06cc\u062f \u0642\u0633\u0645\u062a \u06af\u0632\u06cc\u0646\u0647 \u0647\u0627\u06cc \u0628\u06cc\u0634\u062a\u0631")
    lines.append("")
    lines.append("3\u20e3 \u06af\u0627\u0645 \u0633\u0648\u0645 \u062a\u06cc\u06a9 \u062d\u0627\u0644\u062a \u0642\u062f\u0631\u062a\u0645\u0646\u062f \u06cc\u0627 Beast Mode \u0631\u0648 \u0641\u0639\u0627\u0644 \u06a9\u0646\u06cc\u062f")
    lines.append("")
    lines.append("4\u20e3 \u06af\u0627\u0645 \u0686\u0647\u0627\u0631\u0645 \u0627\u0632 \u0642\u0633\u0645\u062a Connection Protocol \u06cc\u0627 \u067e\u0631\u0648\u062a\u06a9\u0644 \u0627\u062a\u0635\u0627\u0644 \u06af\u0632\u06cc\u0646\u0647 \u0641\u0631\u0627\u0646\u062a\u06cc\u0646\u06af Cdn \u06cc\u0627 CDN Fronting \u0631\u0648 \u0628\u0632\u0646\u06cc\u062f")
    lines.append("")
    lines.append("5\u20e3 \u06af\u0627\u0645 \u0628\u0639\u062f\u06cc \u0627\u0632 \u0642\u0633\u0645\u062a CDN edge IPs \u0622\u06cc\u200c\u067e\u06cc \u0647\u0627\u06cc \u062c\u062f\u06cc\u062f \u06a9\u0627\u0646\u0627\u0644 \u0631\u0648 \u06a9\u0647 \u06af\u0630\u0627\u0634\u062a\u0645 \u0647\u0645\u0634\u0648\u0646\u0648 \u0627\u0648\u0646\u062c\u0627 \u06a9\u067e\u06cc \u067e\u06cc\u0633\u062a \u06a9\u0646\u06cc\u062f")
    lines.append("")
    lines.append("6\u20e3 \u06af\u0627\u0645 \u0622\u062e\u0631 \u0641\u06cc\u0644\u062a\u0631\u0634\u06a9\u0646 \u0634\u06cc\u0631 \u0648 \u062e\u0648\u0631\u0634\u06cc\u062f \u0631\u0648 start \u06a9\u0646\u06cc\u062f \u0686\u0646\u062f \u062b\u0627\u0646\u06cc\u0647 \u0635\u0628\u0631 \u06a9\u0646\u06cc\u062f \u0648\u0635\u0644 \u0645\u06cc\u0634\u0647")
    lines.append("")
    lines.append("\U0001f4e2 @Net4All_None")

    return '\n'.join(lines)


def send_scan_complete(bot_token, chat_id, total_scanned, total_found, all_ips, operator_name=""):
    full_msg = build_message(total_scanned, total_found, all_ips, operator_name)

    if len(full_msg) <= 4000:
        return send_message(bot_token, chat_id, full_msg)

    medals = ["\U0001f947", "\U0001f948", "\U0001f949"]
    top3 = all_ips[:3]

    header = []
    header.append("\U0001f50d IP Scan Complete")
    header.append("")
    header.append("")
    if operator_name:
        header.append("\U0001f4f6 Operator: {}".format(operator_name))
        header.append("")
    header.append("\U0001f4ca Results:")
    header.append("\u2022 Scanned: {}".format(total_scanned))
    header.append("\u2022 Found: {}".format(total_found))
    header.append("")
    header.append("\U0001f3c6 Top 3 Fastest IPs:")
    header.append("")
    for i, ip in enumerate(top3):
        header.append("{} {}".format(medals[i], ip['ip']))
    header.append("")
    header.append("\U0001f4e2 @Net4All_None")

    send_message(bot_token, chat_id, '\n'.join(header))
    _time.sleep(1)

    chunk_size = 50
    total_chunks = (len(all_ips) + chunk_size - 1) // chunk_size

    for i in range(0, len(all_ips), chunk_size):
        chunk = all_ips[i:i + chunk_size]
        idx = i // chunk_size + 1
        is_last = (idx == total_chunks)

        ip_list = "\n".join([ip['ip'] for ip in chunk])

        msg = []
        msg.append("\u2728 \u0644\u06cc\u0633\u062a \u0622\u06cc\u200c\u067e\u06cc ({}/{}):".format(idx, total_chunks))
        msg.append("")
        msg.append("<blockquote expandable><code>{}</code></blockquote>".format(ip_list))

        if is_last:
            msg.append("")
            msg.append("\u2b05\ufe0f \u0647\u0645\u0631\u0648 \u0628\u0627 \u0647\u0645 \u0648\u0627\u0631\u062f \u06a9\u0646\u06cc\u062f \U0001f4f0")
            msg.append("")
            msg.append("\u270f \u0622\u0645\u0648\u0632\u0634 \u0645\u062a\u0646\u06cc :")
            msg.append("")
            msg.append("1\u20e3 \u0646\u0633\u062e\u0647 \u0634\u06cc\u0631 \u062e\u0648\u0631\u0634\u06cc\u062f \u0627\u06af\u0647 \u0627\u0632 \u0642\u0628\u0644 \u062f\u0627\u0631\u06cc\u062f \u062d\u0630\u0641 \u06a9\u0646\u06cc\u062f \u0648 \u0646\u0633\u062e\u0647 \u062c\u062f\u06cc\u062f \u0646\u0635\u0628 \u06a9\u0646\u06cc\u062f")
            msg.append("")
            msg.append("2\u20e3 \u0628\u0631\u06cc\u062f \u0642\u0633\u0645\u062a More Options \u06cc\u0627 \u06af\u0632\u06cc\u0646\u0647 \u0647\u0627\u06cc \u0628\u06cc\u0634\u062a\u0631")
            msg.append("")
            msg.append("3\u20e3 \u062a\u06cc\u06a9 Beast Mode \u0631\u0648 \u0641\u0639\u0627\u0644 \u06a9\u0646\u06cc\u062f")
            msg.append("")
            msg.append("4\u20e3 \u0627\u0632 Connection Protocol \u06af\u0632\u06cc\u0646\u0647 CDN Fronting \u0631\u0648 \u0628\u0632\u0646\u06cc\u062f")
            msg.append("")
            msg.append("5\u20e3 \u0627\u0632 \u0642\u0633\u0645\u062a CDN edge IPs \u0622\u06cc\u200c\u067e\u06cc \u0647\u0627 \u0631\u0648 \u06a9\u067e\u06cc \u067e\u06cc\u0633\u062a \u06a9\u0646\u06cc\u062f")
            msg.append("")
            msg.append("6\u20e3 \u0641\u06cc\u0644\u062a\u0631\u0634\u06a9\u0646 \u0631\u0648 start \u06a9\u0646\u06cc\u062f")
            msg.append("")
            msg.append("\U0001f4e2 @Net4All_None")

        send_message(bot_token, chat_id, '\n'.join(msg))
        _time.sleep(1)

    return True
