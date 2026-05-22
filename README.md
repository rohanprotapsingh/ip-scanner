<div align="center">

# 🔍 IP Scanner - Akamai & Fastly

### Fast CDN IP Scanner with Web UI & Telegram Integration

[![GitHub stars](https://img.shields.io/github/stars/rohanprotapsingh/ip-scanner?style=social)](https://github.com/rohanprotapsingh/ip-scanner)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7+-yellow.svg)](https://python.org)
[![Telegram](https://img.shields.io/badge/Telegram-@Net4All__None-blue?logo=telegram)](https://t.me/Net4All_None)

<p>
  <a href="#-features">Features</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-telegram-integration">Telegram</a> •
  <a href="README_FA.md">🇮🇷 فارسی</a>
</p>

---

</div>

## 🌟 Features

| Feature | Description |
|---------|------------|
| 🌐 **Web Interface** | Beautiful dark-theme UI at `127.0.0.1:9000` |
| ⚡ **Real-time Results** | Live scan results via WebSocket |
| 🏢 **Built-in CDN Ranges** | Akamai & Fastly IP ranges included |
| 📶 **Iranian Operators** | Support for MCI, Irancell, Shatel, Aptel & more |
| 🔍 **Multiple IP Formats** | Single IP, CIDR, Range support |
| 📊 **Sort by Speed** | Results sorted by latency (fastest first) |
| 💾 **Export Results** | Save as TXT, CSV, JSON |
| ![Telegram](https://img.shields.io/badge/-Telegram-blue?logo=telegram&logoColor=white&style=flat-square) **Telegram Bot** | Send results directly to Telegram channel/group |
| 🔐 **Secure** | Bot token stored locally in your browser |
| ⏹ **Stop Anytime** | Cancel scan at any moment |
| 🔎 **CDN Detection** | Auto-detect Akamai, Fastly, Cloudflare |
| 📋 **Copy-friendly** | Mono-format IPs in Telegram with one-click copy |
| 📌 **Topic Support** | Send to specific Telegram group topics |
| 🧩 **Expandable Quote** | Collapsible IP list in Telegram messages |

---

## 📋 Supported IP Formats

```text
Single IP:     1.2.3.4
CIDR:          151.101.0.0/24
Full Range:    23.64.0.1-23.64.0.254
Short Range:   23.64.0.1-254
```

---

## 📶 Supported Operators

| Operator | Name |
|----------|------|
| MCI | Hamrah-e Aval |
| Irancell | MTN Irancell |
| Rightel | Rightel |
| Samantel | Samantel |
| Mokhaberat | TCI |
| Shatel | Shatel |
| Shatel Mobile | Shatel Mobile |
| Aptel | Aptel |
| Asiatech | Asiatech |
| Pishgaman | Pishgaman |

---

## 💻 Installation

### Requirements

- Python 3.7+
- pip

### 🐧 Linux / 📱 Android (Termux)

```bash
pkg update && pkg upgrade -y
pkg install python git -y

git clone https://github.com/istorekala/ip-scanner.git
cd ip-scanner

pip install -r requirements.txt

python app.py
```

> 💡 **Tip:** In Termux notification, tap **Acquire WakeLock** to prevent the app from closing in the background.

### 🪟 Windows

```bash
git clone https://github.com/istorekala/ip-scanner.git
cd ip-scanner

pip install -r requirements.txt

python app.py
```

> Install Python from https://python.org and check **Add Python to PATH**

### 🍎 macOS

```bash
brew install python git

git clone https://github.com/istorekala/ip-scanner.git
cd ip-scanner
pip3 install -r requirements.txt

python3 app.py
```

### After running, open your browser:

```text
http://127.0.0.1:9000
```

---

## 🚀 Usage

### 1️⃣ Select Scan Mode

| Mode | Description |
|------|------------|
| **Custom** | Enter your own IPs manually |
| **Akamai** | Scan built-in Akamai ranges |
| **Fastly** | Scan built-in Fastly ranges |
| **Both** | Scan both Akamai & Fastly |

### 2️⃣ Configure Settings

| Setting | Default | Description |
|---------|---------|-------------|
| Ports | `443, 80` | Ports to scan |
| Threads | `200` | Concurrent connections (max 600) |
| Timeout | `1.5s` | Connection timeout |
| HTTP Check | Off | Enable to detect CDN provider |
| Operator | None | Select your ISP for Telegram message |

### 3️⃣ Start Scan

Click **▶ Start Scan** and watch real-time results appear in the table sorted by speed.

### 4️⃣ Save Results

After scan completes, save results as:

| Format | Description |
|--------|-------------|
| 📄 TXT | Human-readable text file |
| 📊 CSV | Spreadsheet format (Excel compatible) |
| 🔧 JSON | Developer-friendly format |

### 5️⃣ Send to Telegram

1. Run scan **without VPN**
2. After scan completes, **turn on VPN**
3. Click **💬 Send to Telegram**
4. Results will be sent to your channel/group

---

## ![Telegram](https://img.shields.io/badge/-Telegram-blue?logo=telegram&logoColor=white&style=flat-square) Telegram Integration

### Setup Telegram Bot

1. Open [@BotFather](https://t.me/BotFather) in Telegram
2. Send `/newbot`
3. Choose a name and username
4. Copy the **Bot Token**
5. Add bot as **Admin** to your channel/group
6. Give bot permission to **Post Messages**

### Configure in Scanner

1. Check **💬 Telegram** checkbox
2. Enter your **Bot Token**
3. Enter your **Channel/Group ID**
4. Click **💾 Save Settings**
5. Click **🗑 Clear Saved** to remove saved settings

### Channel/Group ID Format

| Type | Format | Example |
|------|--------|---------|
| Public Channel | `@channelname` | `@Net4All_None` |
| Private Group | `-100xxxxxxxxxx` | `-1003475689762` |
| Group + Topic | `-100xxxxxxxxxx:topicID` | `-1003475689762:14` |

### How to Find Group ID

1. Open [Telegram Web](https://web.telegram.org)
2. Go to your group/channel
3. Look at URL: `https://web.telegram.org/a/#-XXXXXXXXXX`
4. Add `-100` before the number

### How to Find Topic ID

1. Open the topic in your group
2. Copy a post link
3. Link format: `https://t.me/c/XXXXXXX/TOPIC_ID/MSG_ID`
4. The middle number is your Topic ID

### Telegram Message Preview

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

✨ Full IP List:

┃ 151.101.9.230
┃ 151.101.5.108
┃ ...
┃ ▼ Show more

📢 @Net4All_None
```

---

## 📁 Project Structure

```text
ip-scanner/
├── app.py              # Flask web server & socket events
├── engine.py           # Scan engine
├── utils.py            # IP parser & CDN detection
├── saver.py            # Save results
├── telegram_bot.py     # Telegram integration
├── config.py           # Settings, ranges & operators
├── page.py             # Web UI
├── requirements.txt    # Dependencies
├── .gitignore          # Ignore rules
├── README.md           # English documentation
└── README_FA.md        # Persian documentation
```

---

## ⚙️ Configuration

Edit `config.py` to customize:

```python
DEFAULT_PORTS = [443, 80]
DEFAULT_THREADS = 200
DEFAULT_TIMEOUT = 1.5
MAX_THREADS = 600
SERVER_PORT = 9000
```

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| Page not loading | Make sure port 9000 is free |
| Scan too slow | Reduce timeout, increase threads |
| Telegram not sending | Check token and bot admin access |
| Stop not working | Wait a few seconds for threads to stop |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |

---

## 🤝 Contributing

1. Fork the repository
2. Create your branch: `git checkout -b feature/amazing`
3. Commit changes: `git commit -m "Add amazing feature"`
4. Push branch: `git push origin feature/amazing`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

<div align="center">

### ⭐ Star this repo if you find it useful!

[![Telegram](https://img.shields.io/badge/Join-Telegram%20Channel-blue?style=for-the-badge&logo=telegram)](https://t.me/Net4All_None)
[![GitHub](https://img.shields.io/badge/Follow-GitHub-black?style=for-the-badge&logo=github)](https://github.com/rohanprotapsingh)

**Made with ❤️ by [@Net4All_None](https://t.me/Net4All_None)**

</div>
