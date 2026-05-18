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
    medals = ["🥇", "🥈", "🥉"]
    top3 = all_ips[:3]

    header = []
    header.append("🔍 <b>IP Scan Complete</b>")
    header.append("")
    if operator_name:
        header.append("📡 <b>Operator:</b> {}".format(operator_name))
        header.append("")
    header.append("📊 <b>Results:</b>")
    header.append("• Scanned: <code>{}</code>".format(total_scanned))
    header.append("• Found: <code>{}</code>".format(total_found))
    header.append("")
    header.append("🏆 <b>Top 3 Fastest IPs:</b>")
    header.append("")
    for i, ip in enumerate(top3):
        header.append("{} <code>{}</code>".format(medals[i], ip['ip']))

    ip_lines = [ip['ip'] for ip in all_ips]
    ip_block = "\n".join(ip_lines)

    full = list(header)
    full.append("")
    full.append("")
    full.append("✨ <b>لیست کامل آی‌پی :</b>")
    full.append("")
    full.append("<blockquote>{}</blockquote>".format(ip_block))
    full.append("")
    full.append("⬅️ همرو با هم وارد کنید 📰")
    full.append("")
    full.append("✏ <b>آموزش متنی :</b>")
    full.append("")
    full.append("1⃣ نسخه شیر خورشید اگه از قبل دارید حذف کنید و نسخه جدید نصب کنید")
    full.append("")
    full.append("2⃣ گام دوم برید قسمت More Options یا اگه زبان فارسی هستید برید قسمت گزینه های بیشتر")
    full.append("")
    full.append("3⃣ گام سوم تیک حالت قدرتمند یا Beast Mode رو فعال کنید")
    full.append("")
    full.append("4⃣ گام چهارم از قسمت Connection Protocol یا پروتکل اتصال گزینه فرانتینگ Cdn یا CDN Fronting رو بزنید")
    full.append("")
    full.append("5⃣ گام بعدی از قسمت CDN edge IPs آی‌پی های جدید کانال رو که گذاشتم همشونو اونجا کپی پیست کنید")
    full.append("")
    full.append("6⃣ گام آخر فیلترشکن شیر و خورشید رو start کنید چند ثانیه صبر کنید وصل میشه")
    full.append("")
    full.append("📢 @Net4All_none")

    full_msg = '\n'.join(full)

    if len(full_msg) <= 4000:
        return send_message(bot_token, chat_id, full_msg)

    send_message(bot_token, chat_id, '\n'.join(header) + "\n\n📢 @Net4All_none")

    chunk_size = 50
    for i in range(0, len(all_ips), chunk_size):
        chunk = all_ips[i:i + chunk_size]
        idx = i // chunk_size + 1
        total_chunks = (len(all_ips) + chunk_size - 1) // chunk_size
        is_last = (idx == total_chunks)

        msg = []
        msg.append("✨ <b>لیست آی‌پی ({}/{}):</b>".format(idx, total_chunks))
        msg.append("")
        msg.append("<blockquote>{}</blockquote>".format(
            '\n'.join([ip['ip'] for ip in chunk])
        ))

        if is_last:
            msg.append("")
            msg.append("⬅️ همرو با هم وارد کنید 📰")
            msg.append("")
            msg.append("✏ <b>آموزش متنی :</b>")
            msg.append("")
            msg.append("1⃣ نسخه شیر خورشید اگه از قبل دارید حذف کنید و نسخه جدید نصب کنید")
            msg.append("")
            msg.append("2⃣ برید قسمت More Options")
            msg.append("")
            msg.append("3⃣ تیک Beast Mode رو فعال کنید")
            msg.append("")
            msg.append("4⃣ از Connection Protocol گزینه CDN Fronting رو بزنید")
            msg.append("")
            msg.append("5⃣ از قسمت CDN edge IPs آی‌پی ها رو کپی پیست کنید")
            msg.append("")
            msg.append("6⃣ فیلترشکن رو start کنید")
            msg.append("")
            msg.append("📢 @Net4All_none")

        send_message(bot_token, chat_id, '\n'.join(msg))
        _time.sleep(1)

    return True
