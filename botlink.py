#!/usr/bin/env python3
# ============================================
# TELEGRAM BOT SCANNER - ULTRA HACKER EDITION V2
# Dev: @lagatech
# Features: Matrix UI, Webapp Grabber, Webhook Detector, Mass Scan
# ============================================

import asyncio
import os
import time
import random
import datetime
from telethon import TelegramClient, functions, types
from telethon.errors import SessionPasswordNeededError, UsernameNotOccupiedError, UsernameInvalidError
from telethon.tl import types as tl_types

# Cross-platform color support
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    GREEN = Fore.GREEN
    RED = Fore.RED
    CYAN = Fore.CYAN
    YELLOW = Fore.YELLOW
    MAGENTA = Fore.MAGENTA
    WHITE = Fore.WHITE
    RESET = Style.RESET_ALL
except ImportError:
    print("[-] Installing colorama for colors...")
    os.system("pip install colorama")
    from colorama import init, Fore, Style
    init(autoreset=True)
    GREEN = Fore.GREEN
    RED = Fore.RED
    CYAN = Fore.CYAN
    YELLOW = Fore.YELLOW
    MAGENTA = Fore.MAGENTA
    WHITE = Fore.WHITE
    RESET = Style.RESET_ALL

# =============================
# Config
# =============================
SESSION_NAME = "hacker_session"
CONFIG_FILE = "config.txt"
REPORT_DIR = "intel_reports"

# =============================
# Hacker UI System
# =============================

def print_logo():
    os.system("clear" if os.name != "nt" else "cls")
    logo = f"""{GREEN}
██╗      █████╗  ██████╗  █████╗ ████████╗███████╗ ██████╗██╗  ██╗
██║     ██╔══██╗██╔════╝ ██╔══██╗╚══██╔══╝██╔════╝██╔════╝██║  ██║
██║     ███████║██║  ███╗███████║   ██║   █████╗  ██║     ███████║
██║     ██╔══██║██║   ██║██╔══██║   ██║   ██╔══╝  ██║     ██╔══██║
███████╗██║  ██║╚██████╔╝██║  ██║   ██║   ███████╗╚██████╗██║  ██║
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝
        {CYAN}TELEGRAM BOT SCANNER - ULTRA EDITION V2{RESET}
        {YELLOW}💀 [DEV: @lagatech] | [FEATURES: WEBHOOK, WEBAPP, MASS SCAN]{RESET}
"""
    print(logo)

def matrix_effect(lines=5):
    """Simulates matrix rain for dramatic effect"""
    chars = "01@#$%^&*abcdef"
    for _ in range(lines):
        line = "".join(random.choice(chars) for _ in range(40))
        print(f"{GREEN}{line}{RESET}")
        time.sleep(0.05)

def loading_bar(text="Scanning", duration=2):
    symbols = ["▏", "▎", "▍", "▌", "▋", "▊", "▉", "█"]
    steps = 20
    print(f"{CYAN}{text}: ", end="")
    for i in range(steps):
        time.sleep(duration / steps)
        progress = int((i + 1) / steps * 100)
        bar_fill = int((i + 1) / steps * 10)
        bar = "█" * bar_fill + " " * (10 - bar_fill)
        print(f"{GREEN}[{bar}] {progress}%{RESET}", end="\r")
    print(f"{GREEN}[██████████] 100%{RESET} - Complete")

# =============================
# API System
# =============================

def get_api():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE) as f:
            lines = f.read().splitlines()
            if len(lines) >= 2:
                return lines[0], lines[1]

    print(YELLOW + "\n[!] API Configuration Required\n" + RESET)
    api_id = input("API ID  : ")
    api_hash = input("API HASH: ")

    with open(CONFIG_FILE, "w") as f:
        f.write(f"{api_id}\n{api_hash}")
    
    return api_id, api_hash

# =============================
# Intelligence Functions
# =============================

def detect_webhooks(text):
    """Detects potential webhook URLs in text"""
    hooks = []
    keywords = ["webhook", "api/webhooks", "discord.com/api", "discohook", "glitch"]
    if text:
        for line in text.split('\n'):
            if "http" in line and any(k in line.lower() for k in keywords):
                hooks.append(line.strip())
    return hooks

async def scan_single_bot(client, bot_username, save_report=False):
    try:
        # Phase 1: Identification
        loading_bar(f"Identifying {bot_username}", 1)
        
        entity = await client.get_entity(bot_username)
        
        # Check if it's actually a bot
        if not entity.bot:
            print(f"{RED}[!] @{bot_username} is not a bot!{RESET}")
            return

        # Phase 2: Deep Scan
        result = await client(functions.users.GetFullUserRequest(id=entity))
        user = result.users[0]
        bot_info = result.full_user.bot_info

        report_data = []
        header = f"\n{GREEN}════════════════ 🤖 BOT INTEL 🤖 ════════════════{RESET}"
        print(header)
        
        # Basic Intel
        name = user.first_name + (user.last_name or "")
        username = f"@{user.username}" if user.username else "None"
        user_id = user.id
        
        print(f"{CYAN}🆔 Bot ID     :{RESET} {user_id}")
        print(f"{CYAN}📛 Name       :{RESET} {name}")
        print(f"{CYAN}👤 Username   :{RESET} {username}")
        print(f"{CYAN}✅ Verified   :{RESET} {GREEN}Yes{RESET}" if user.verified else f"{CYAN}✅ Verified   :{RESET} {RED}No{RESET}")
        print(f"{CYAN}⚠️ Scam Flag  :{RESET} {RED}Yes{RESET}" if user.scam else f"{CYAN}⚠️ Scam Flag  :{RESET} {GREEN}Clean{RESET}")

        # WebApp & Menu Link Detection
        print(f"\n{YELLOW}[>] Analyzing Access Points...{RESET}")
        
        webapp_found = False
        
        # 1. Check Menu Button
        if bot_info and bot_info.menu_button:
            menu = bot_info.menu_button
            if isinstance(menu, types.BotMenuButton):
                print(f"{GREEN}🔗 Menu Button :{RESET} {menu.url}")
                report_data.append(f"Menu URL: {menu.url}")
                webapp_found = True

        # 2. Check Description for hidden links
        desc = bot_info.description if bot_info else ""
        if "http" in desc:
            print(f"{MAGENTA}🌐 Description Links Found:{RESET}")
            import re
            links = re.findall(r'(https?://[^\s]+)', desc)
            for link in links:
                print(f"   -> {link}")
                report_data.append(f"Desc Link: {link}")
                
                # Webhook Check
                hooks = detect_webhooks(link)
                if hooks:
                    print(f"{RED}💀 WEBHOOK DETECTED!{RESET}")
                    for h in hooks:
                        print(f"   {RED}[!] {h}{RESET}")

        # 3. Check Inline Buttons (Common for WebApps)
        # Note: Real-time message checking would require interacting with the bot.
        # This static analysis focuses on available metadata.

        # Commands Analysis
        if bot_info and bot_info.commands:
            print(f"\n{YELLOW}[>] Parsing Bot Commands...{RESET}")
            for cmd in bot_info.commands[:10]: # Limit output
                print(f"   💻 /{cmd.command} - {cmd.description}")
        
        print(f"{GREEN}══════════════════════════════════════════════════{RESET}")
        
        # Save Report Logic
        if save_report:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{REPORT_DIR}/{bot_username}_{timestamp}.txt"
            os.makedirs(REPORT_DIR, exist_ok=True)
            with open(filename, "w") as f:
                f.write(f"BOT INTEL REPORT\n")
                f.write(f"Target: {username}\nID: {user_id}\n")
                f.write(f"Verified: {user.verified}\nScam: {user.scam}\n")
                f.write(f"Description:\n{desc}\n")
            print(f"{CYAN}[💾] Report saved to {filename}{RESET}")

    except Exception as e:
        print(f"{RED}[ERROR] Failed to scan {bot_username}: {str(e)}{RESET}")

async def mass_scan(client):
    print(f"{YELLOW}\n[!] MASS BOT SCANNER [!]{RESET}")
    print("Enter bot usernames separated by space or comma (or file.txt):")
    targets_input = input(f"{CYAN}Targets > {RESET}").strip()
    
    targets = []
    if targets_input.endswith(".txt") and os.path.exists(targets_input):
        with open(targets_input, "r") as f:
            targets = [line.strip() for line in f if line.strip()]
    else:
        targets = [t.strip() for t in targets_input.replace(',', ' ').split()]
    
    print(f"{GREEN}[*] Queued {len(targets)} bots for scanning...{RESET}")
    matrix_effect(3)
    
    for bot in targets:
        await scan_single_bot(client, bot, save_report=True)
        time.sleep(1) # Prevent flooding

async def search_crawler(client):
    """Auto Bot Finder (Telegram search crawler)"""
    query = input(f"{CYAN}Enter Search Keyword > {RESET}")
    print(f"{YELLOW}[*] Searching Telegram for bots matching: {query}...{RESET}")
    
    try:
        # Using messages.searchGlobal to find public bots
        result = await client(functions.messages.SearchGlobalRequest(
            q=query,
            filter=types.InputMessagesFilterEmpty(),
            min_date=0,
            max_date=0,
            offset_rate=0,
            offset_peer=types.InputPeerEmpty(),
            offset_id=0,
            limit=20
        ))
        
        found_bots = set()
        # Iterate through found chats/users
        for chat in result.chats:
            if hasattr(chat, 'bot') and chat.bot:
                found_bots.add(chat.username)
        
        if found_bots:
            print(f"{GREEN}[+] Found {len(found_bots)} bots!{RESET}")
            for bot in found_bots:
                print(f"   - @{bot}")
            
            choice = input(f"\n{CYAN}Scan all found bots? (y/n) > {RESET}")
            if choice.lower() == 'y':
                for bot in found_bots:
                    await scan_single_bot(client, bot)
        else:
            print(f"{RED}[-] No bots found for this keyword.{RESET}")
            
    except Exception as e:
        print(f"{RED}[ERROR] Search failed: {e}{RESET}")

# =============================
# MAIN SYSTEM
# =============================

async def main():

    print_logo()
    
    # Create report dir
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)

    api_id, api_hash = get_api()

    client = TelegramClient(SESSION_NAME, api_id, api_hash)

    print(f"{CYAN}[*] Connecting to Telegram Servers...{RESET}")
    await client.connect()

    if not await client.is_user_authorized():
        print(YELLOW + "\n[!] New Login Required\n" + RESET)
        phone = input("📱 Phone Number (with country code): ")
        
        try:
            await client.send_code_request(phone)
            code = input("🔑 Enter OTP: ")
            
            try:
                await client.sign_in(phone, code)
            except SessionPasswordNeededError:
                password = input("🔒 2FA Password: ")
                await client.sign_in(password=password)
                
            print(GREEN + "\n[✓] Login Successful!" + RESET)
            
        except Exception as e:
            print(RED + f"\n[!] Login Failed: {e}" + RESET)
            return

    # Main Menu
    while True:
        print(f"\n{WHITE}══════════════ 💀 MAIN MENU 💀 ══════════════{RESET}")
        print(f"  {CYAN}1.{RESET} Scan Single Bot")
        print(f"  {CYAN}2.{RESET} Mass Bot Scanner (List/File)")
        print(f"  {CYAN}3.{RESET} Auto Bot Finder (Search Crawler)")
        print(f"  {CYAN}4.{RESET} Exit")
        print(f"{WHITE}═══════════════════════════════════════════════{RESET}")
        
        choice = input(f"{MAGENTA}Select Option > {RESET}")

        if choice == "1":
            target = input(f"{CYAN}Enter Bot Username > {RESET}")
            await scan_single_bot(client, target, save_report=True)
        
        elif choice == "2":
            await mass_scan(client)
        
        elif choice == "3":
            await search_crawler(client)
        
        elif choice == "4":
            print(f"{GREEN}\n[👋] Closing Connection. Goodbye, Hacker.{RESET}")
            break
        
        else:
            print(f"{RED}[!] Invalid Option{RESET}")

    await client.disconnect()

# =============================
# RUN
# =============================

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Force Closed by User{RESET}")
