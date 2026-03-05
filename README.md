<h1 align="center">
  <a href="https://github.com/n3xupx-gif/botlink-">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=28&duration=4000&pause=1000&color=2E9EF3&center=true&vCenter=true&random=false&width=435&lines=TELEGRAM+BOT+SCANNER;ULTRA+HUNTER+EDITION;by+%40lagatech" alt="Typing SVG" />
  </a>
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Version-2.0.0-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3.9+-green?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Telethon-Latest-red?style=for-the-badge&logo=telegram" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" />
</p>

<p align="center">
  <i>A powerful Python tool to scan Telegram bots, extract hidden web-links, and download website source code automatically.</i>
</p>

---

## 📸 **Preview**

<img src="https://i.imgur.com/YourImageLinkHere.png" alt="Tool Preview" width="100%">

> *Note: Replace the image link above with an actual screenshot of your tool running to make the README pop.*

---

## 🚀 **Features**

- **🤖 Bot Scanning:** Retrieves detailed information about any Telegram bot (ID, Name, Verified Status, Scam Flags).
- **🔗 Link Extraction:** Automatically detects and extracts `Menu Button` URLs and web-app links.
- **📥 Source Downloader:** Saves the HTML/JS source code of the bot's linked website directly to your device.
- **🎨 Cool UI:** Features animated loading spinners, progress bars, and color-coded outputs.
- **🔐 Secure Login:** Saves API credentials locally in `config.txt` (Gitignored for security).
- **📚 Beginner Friendly:** Built-in guide showing exactly where to get API ID and Hash.

---

## 📂 **Project Structure**

```bash
botlink-/
├── bot_scanner.py      # Main script file
├── config.txt          # Auto-generated API credentials
├── sessions/           # Telethon session files
└── README.md           # Documentation
```

---

## 🛠️ **Installation & Setup**

### **Prerequisites**
- Python 3.9 or higher installed.
- A Telegram Account.
- `api_id` and `api_hash` from [my.telegram.org](https://my.telegram.org).

### **Step 1: Clone the Repository**
Open your terminal and run:
```bash
git clone https://github.com/n3xupx-gif/botlink-.git
cd botlink-
```

### **Step 2: Install Requirements**
Install the necessary Python libraries:
```bash
pip install telethon requests
```

### **Step 3: Run the Tool**
```bash
python3 bot_scanner.py
```

---

## ⚙️ **Usage Guide**

### **1. API Credentials (One-Time Setup)**
When you run the tool for the first time, it will ask for credentials.

> **Where to get them?**
> 1. Go to **[https://my.telegram.org](https://my.telegram.org)**.
> 2. Log in with your phone number.
> 3. Click **"API development tools"**.
> 4. Create a new application (fill in any name).
> 5. Copy your `api_id` and `api_hash` and paste them into the tool.

### **2. OTP Login**
- The tool will send an OTP to your **Telegram App** (not SMS usually).
- Enter the code to log in.
- If you have Two-Step Verification (2FA) enabled, enter your password.

### **3. Scanning a Bot**
- Enter the **Username** of the bot (e.g., `@BotFather`).
- The tool will display detailed info.

### **4. Downloading Website Code**
- If the bot has a `Menu Button` or `Web App` link:
  - The tool will ask: **"Do you want to download the website code?"**
  - Type `yes`.
  - Enter a file name (e.g., `my_bot_site`).
  - The file will be saved as an `.html` file in the current directory.

---

## 💡 **Example Output**

```text
╔══════════════════════════════╗
║        🤖 BOT INFO           ║
╚══════════════════════════════╝
👤 Name      : BotFather
🔗 Username  : @BotFather
🆔 Bot ID    : 93372553
✅ Verified  : True
🚩 Scam Flag : False

🌐 Website Link Found: https://core.telegram.org/bots

[?] Do you want to download the website code?
Type 'yes' to download: yes
📝 Enter file name: botfather_page

Downloading: [████████████████████] 100%
✅ SUCCESS!
File saved as: botfather_page.html
```

---

## ⚠️ **Disclaimer**

> **Educational Purpose Only**: This tool is intended for educational purposes and legitimate security research. Do not use it to download copyrighted material or for any illegal activities. The developer (@lagatech) is not responsible for any misuse of this software.

---

## 👨‍💻 **Developer**

<h3 align="center">LAGATECH</h3>
<p align="center">
  <a href="https://t.me/lagatech"><img src="https://img.shields.io/badge/Telegram-Channel-blue?style=for-the-badge&logo=telegram" /></a>
</p>

---

<p align="center">
  <b>Made with ❤️ and Python</b><br>
  <i>If you like this project, give it a ⭐!</i>
</p>
