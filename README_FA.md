<div align="center">

# 🔍 اسکنر آی‌پی - آکامای و فستلی

### اسکنر سریع CDN با رابط وب و ارسال به تلگرام

[![GitHub stars](https://img.shields.io/github/stars/rohanprotapsingh/ip-scanner?style=social)](https://github.com/rohanprotapsingh/ip-scanner)
[![Python](https://img.shields.io/badge/python-3.7+-yellow.svg)](https://python.org)
[![Telegram](https://img.shields.io/badge/تلگرام-@Net4All__None-blue?logo=telegram)](https://t.me/Net4All_None)

<p>
  <a href="#-ویژگیها">ویژگی‌ها</a> •
  <a href="#-نصب-و-راهاندازی">نصب</a> •
  <a href="#-نحوه-استفاده">استفاده</a> •
  <a href="#-تنظیم-تلگرام">تلگرام</a> •
  <a href="README.md">English</a>
</p>

---

</div>

## ✨ ویژگی‌ها

| ویژگی | توضیح |
|-------|-------|
| 🌐 **رابط وب** | طراحی زیبا و تاریک در آدرس `127.0.0.1:9000` |
| ⚡ **نتایج لحظه‌ای** | نمایش زنده نتایج اسکن |
| 🏢 **رنج‌های داخلی** | رنج آی‌پی‌های آکامای و فستلی از قبل وارد شده |
| 📶 **اپراتورهای ایرانی** | همراه اول، ایرانسل، شاتل، آپتل و ... |
| 🔍 **فرمت‌های مختلف** | تک آی‌پی، CIDR، رنج |
| 📊 **مرتب‌سازی** | نتایج بر اساس سرعت (سریع‌ترین اول) |
| 💾 **ذخیره نتایج** | خروجی TXT، CSV، JSON |
| ![Telegram](https://img.shields.io/badge/-Telegram-blue?logo=telegram&logoColor=white&style=flat-square) **ربات تلگرام** | ارسال مستقیم نتایج به کانال/گروه |
| 🔐 **امن** | توکن ربات فقط در مرورگر شما ذخیره می‌شود |
| ⏹ **توقف آنی** | قابلیت متوقف کردن اسکن در هر لحظه |
| 🔎 **تشخیص CDN** | تشخیص خودکار Akamai، Fastly، Cloudflare |
| 📋 **کپی آسان** | لیست آی‌پی با فرمت mono و کپی با یک کلیک |
| 📌 **پشتیبانی تاپیک** | ارسال به تاپیک خاص در گروه تلگرام |
| 🧩 **نقل‌قول جمع‌شونده** | لیست آی‌پی به صورت جمع‌شونده در تلگرام |

---

## 📋 فرمت‌های ورودی آی‌پی

```text
تک آی‌پی:      1.2.3.4
CIDR:          151.101.0.0/24
رنج کامل:      23.64.0.1-23.64.0.254
رنج کوتاه:     23.64.0.1-254
```

---

## 📶 اپراتورهای پشتیبانی شده

| اپراتور | نام |
|---------|-----|
| همراه اول | MCI |
| ایرانسل | MTN Irancell |
| رایتل | Rightel |
| سامانتل | Samantel |
| مخابرات | TCI |
| شاتل | Shatel |
| شاتل موبایل | Shatel Mobile |
| آپتل | Aptel |
| آسیاتک | Asiatech |
| پیشگامان | Pishgaman |

---

## 💻 نصب و راه‌اندازی

### پیش‌نیازها

- Python 3.7+
- pip

### 📱 اندروید (ترموکس)

```bash
pkg update && pkg upgrade -y
pkg install python git -y

git clone https://github.com/istorekala/ip-scanner.git
cd ip-scanner

pip install -r requirements.txt

python app.py
```

> 💡 **نکته:** از نوار اعلان ترموکس روی **Acquire WakeLock** بزنید تا برنامه در پس‌زمینه بسته نشود.

### 🪟 ویندوز

```bash
git clone https://github.com/istorekala/ip-scanner.git
cd ip-scanner

pip install -r requirements.txt

python app.py
```

> پایتون را از https://python.org نصب کنید و تیک **Add Python to PATH** را بزنید.

### 🍎 مک

```bash
brew install python git

git clone https://github.com/istorekala/ip-scanner.git
cd ip-scanner
pip3 install -r requirements.txt

python3 app.py
```

### بعد از اجرا مرورگر را باز کنید:

```text
http://127.0.0.1:9000
```

---

## 🚀 نحوه استفاده

### ۱️⃣ انتخاب حالت اسکن

| حالت | توضیح |
|------|-------|
| **Custom** | وارد کردن دستی آی‌پی |
| **Akamai** | اسکن رنج‌های آکامای |
| **Fastly** | اسکن رنج‌های فستلی |
| **Both** | اسکن هر دو |

### ۲️⃣ تنظیمات

| تنظیم | پیش‌فرض | توضیح |
|------|---------|-------|
| Ports | `443, 80` | پورت‌های اسکن |
| Threads | `200` | تعداد اتصال همزمان |
| Timeout | `1.5s` | زمان انتظار |
| HTTP Check | خاموش | برای تشخیص CDN |
| Operator | none | انتخاب اپراتور |

### ۳️⃣ شروع اسکن

روی **▶ Start Scan** کلیک کنید و نتایج را به صورت زنده ببینید.

### ۴️⃣ ذخیره نتایج

بعد از اتمام اسکن، نتایج را در فرمت‌های زیر ذخیره کنید:

| فرمت | توضیح |
|------|-------|
| 📄 TXT | فایل متنی ساده |
| 📊 CSV | مناسب اکسل |
| 🔧 JSON | مناسب توسعه‌دهنده |

### ۵️⃣ ارسال به تلگرام

1. اسکن را **بدون فیلترشکن** انجام دهید
2. بعد از اتمام اسکن **فیلترشکن را روشن کنید**
3. روی **💬 Send to Telegram** بزنید
4. نتایج به کانال/گروه شما ارسال می‌شود

---

## ![Telegram](https://img.shields.io/badge/-Telegram-blue?logo=telegram&logoColor=white&style=flat-square) تنظیم تلگرام

### ساخت ربات

1. در تلگرام وارد [@BotFather](https://t.me/BotFather) شوید
2. دستور `/newbot` را بفرستید
3. برای ربات اسم و یوزرنیم انتخاب کنید
4. **توکن ربات** را کپی کنید
5. ربات را **ادمین** کانال/گروه کنید
6. دسترسی **ارسال پیام** را به ربات بدهید

### تنظیم در اسکنر

1. تیک **💬 Telegram** را بزنید
2. **Bot Token** را وارد کنید
3. **Channel/Group ID** را وارد کنید
4. روی **💾 Save Settings** بزنید
5. برای پاک کردن، روی **🗑 Clear Saved** بزنید

### فرمت آیدی

| نوع | فرمت | مثال |
|-----|------|------|
| کانال عمومی | `@نام_کانال` | `@Net4All_None` |
| گروه خصوصی | `-100xxxxxxxxxx` | `-1003475689762` |
| گروه + تاپیک | `-100xxxxxxxxxx:شماره_تاپیک` | `-1003475689762:14` |

### پیدا کردن آیدی گروه

1. وارد [Telegram Web](https://web.telegram.org) شوید
2. وارد گروه یا کانال شوید
3. به آدرس مرورگر نگاه کنید: `https://web.telegram.org/a/#-XXXXXXXXXX`
4. قبل از عدد، `-100` اضافه کنید

### پیدا کردن آیدی تاپیک

1. تاپیک موردنظر را باز کنید
2. لینک یکی از پیام‌ها را کپی کنید
3. فرمت لینک: `https://t.me/c/XXXXXXX/TOPIC_ID/MSG_ID`
4. عدد وسط، آیدی تاپیک است

### نمونه پیام در تلگرام

```text
🔍 IP Scan Complete

📶 Operator: Hamrah-e Aval (MCI)

📊 Results:
• Scanned: 500
• Found: 127

🏆 Top 3 Fastest IPs:

🥇 151.101.9.230
🥈 151.101.5.108
🥉 151.101.5.181

✨ لیست کامل آی‌پی :

┃ 151.101.9.230
┃ 151.101.5.108
┃ ...
┃ ▼ Show more

📢 @Net4All_None
```

---

## 📁 ساختار پروژه

```text
ip-scanner/
├── app.py              # سرور Flask و رویدادها
├── engine.py           # موتور اسکن
├── utils.py            # پارس آی‌پی و تشخیص CDN
├── saver.py            # ذخیره نتایج
├── telegram_bot.py     # اتصال به تلگرام
├── config.py           # تنظیمات و رنج‌ها و اپراتورها
├── page.py             # رابط کاربری وب
├── requirements.txt    # وابستگی‌ها
├── .gitignore          # فایل‌های نادیده گرفته شده
├── README.md           # راهنمای انگلیسی
└── README_FA.md        # راهنمای فارسی
```

---

## ⚙️ تنظیمات

در فایل `config.py` می‌توانید این مقادیر را تغییر دهید:

```python
DEFAULT_PORTS = [443, 80]
DEFAULT_THREADS = 200
DEFAULT_TIMEOUT = 1.5
MAX_THREADS = 600
SERVER_PORT = 9000
```

---

## 🔧 رفع مشکلات رایج

| مشکل | راه‌حل |
|------|--------|
| صفحه باز نمی‌شود | مطمئن شوید پورت 9000 آزاد است |
| اسکن کند است | Timeout را کمتر و Threads را بیشتر کنید |
| تلگرام پیام نمی‌فرستد | توکن و ادمین بودن ربات را بررسی کنید |
| Stop درست کار نمی‌کند | چند ثانیه برای توقف کامل صبر کنید |
| `ModuleNotFoundError` | دستور `pip install -r requirements.txt` را اجرا کنید |

---

## 🤝 مشارکت

1. پروژه را Fork کنید
2. شاخه جدید بسازید: `git checkout -b feature/amazing`
3. تغییرات را Commit کنید: `git commit -m "Add amazing feature"`
4. Push کنید: `git push origin feature/amazing`
5. Pull Request باز کنید

---

## 📄 لایسنس

این پروژه تحت لایسنس MIT منتشر شده است.

---

<div align="center">

### ⭐ اگر این پروژه برای شما مفید بود، به آن ستاره بدهید!

[![Telegram](https://img.shields.io/badge/عضویت-کانال%20تلگرام-blue?style=for-the-badge&logo=telegram)](https://t.me/Net4All_None)
[![GitHub](https://img.shields.io/badge/دنبال%20کردن-GitHub-black?style=for-the-badge&logo=github)](https://github.com/rohanprotapsingh)

**ساخته شده با ❤️ توسط [@Net4All_None](https://t.me/Net4All_None)**

</div>
