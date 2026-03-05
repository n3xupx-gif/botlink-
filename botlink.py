#!/usr/bin/env python3
# ============================================
# TELEGRAM BOT SCANNER - ULTRA HUNTER EDITION
# Dev: @lagatech
# Feature: Web Source Downloader & Pro UI
# ============================================

import asyncio
import os
import sys
import time
import requests
from telethon import TelegramClient, functions, types
from telethon.errors import SessionPasswordNeededError

# =============================
# Colors & Styles
# =============================

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

# =============================
# Updated Logo
# =============================

logo = f"""{GREEN}
{BOLD}
██╗      █████╗  ██████╗  █████╗ ████████╗███████╗ ██████╗██╗  ██╗
██║     ██╔══██╗██╔════╝ ██╔══██╗╚══██╔══╝██╔════╝██╔════╝██║  ██║
██║     ███████║██║  ███╗███████║   ██║   █████╗  ██║     ███████║
██║     ██╔══██║██║   ██║██╔══██║   ██║   ██╔══╝  ██║     ██╔══██║
███████╗██║  ██║╚██████╔╝██║  ██║   ██║   ███████╗╚██████╗██║  ██║
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝

      ⚡ TELEGRAM BOT SCANNER & DOWNLOADER ⚡
           ULTRA EDITION v2.0

        DEV : @lagatech
{RESET}
"""

# =============================
# Advanced Animation System
# =============================

def print_banner():
    os.system("clear")
    print(logo)

def animate_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_spin(text="Processing", duration=3):
    animation_frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        frame = animation_frames[i % len(animation_frames)]
        print(f"{CYAN}{frame} {text}...{RESET}", end="\r")
        time.sleep(0.1)
        i += 1
    print(f"{GREEN}✔ {text} Complete!    {RESET}")

def progress_bar(task="Downloading", duration=5):
    bar_length = 40
    for i in range(bar_length + 1):
        time.sleep(duration / bar_length)
        percent = 100 * i // bar_length
        filled = '█' * i
        empty = '░' * (bar_length - i)
        sys.stdout.write(f'\r{CYAN}{task}: [{YELLOW}{filled}{CYAN}{empty}] {GREEN}{percent}%{RESET}')
        sys.stdout.flush()
    print()

# =============================
# API System with Guide
# =============================

def get_api():
    if os.path.exists("config.txt"):
        with open("config.txt") as f:
            lines = f.read().splitlines()
            api_id = lines[0].strip()
            api_hash = lines[1].strip()
            return api_id, api_hash

    print(f"{YELLOW}{BOLD}{'='*50}")
    print(" ⚠️  API CREDENTIALS REQUIRED")
    print(f"{'='*50}{RESET}\n")
    
    print(f"{CYAN}[ GUIDE ] Where to get API ID & HASH?{RESET}")
    print(f"1. Visit: {UNDERLINE}https://my.telegram.org{RESET}")
    print(f"2. Login with your Phone Number (Telegram will send OTP to your Telegram App).")
    print(f"3. Click on {BOLD}'API development tools'{RESET}.")
    print(f"4. Fill the form (App title & Short name can be anything).")
    print(f"5. Copy your {GREEN}api_id{RESET} and {GREEN}api_hash{RESET} here.\n")

    api_id = input(f"{BOLD}👉 Enter API ID : {RESET}")
    api_hash = input(f"{BOLD}👉 Enter API HASH : {RESET}")

    with open("config.txt", "w") as f:
        f.write(api_id + "\n")
        f.write(api_hash + "\n")
    
    print(f"\n{GREEN}Credentials Saved Successfully!{RESET}\n")
    return api_id, api_hash

# =============================
# Web Downloader Function
# =============================

def download_website(url, filename):
    try:
        if not url.startswith("http"):
            url = "https://" + url

        print(f"\n{CYAN}[*] Connecting to server...{RESET}")
        
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            # Add .html extension if not present
            if not filename.endswith(('.html', '.htm', '.php')):
                filename += ".html"

            progress_bar(task=f"Saving {filename}", duration=2)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(response.text)
            
            print(f"\n{GREEN}{BOLD}✅ SUCCESS!{RESET}")
            print(f"File saved as: {YELLOW}{filename}{RESET}")
            print(f"Size: {len(response.text)} bytes")
        else:
            print(f"{RED}❌ Failed to download. Server returned code: {response.status_code}{RESET}")

    except Exception as e:
        print(f"{RED}[ERROR] Connection Failed: {e}{RESET}")

# =============================
# Bot Scanner
# =============================

async def scan_bot(client, bot_username):
    try:
        loading_spin("Fetching Bot Data", 2)
        
        bot = await client.get_entity(bot_username)
        result = await client(functions.users.GetFullUserRequest(id=bot))
        user = result.users[0]
        bot_info = result.full_user.bot_info

        print(f"\n{GREEN}{BOLD}╔══════════════════════════════╗")
        print(f"║        🤖 BOT INFO           ║")
        print(f"╚══════════════════════════════╝{RESET}")

        print(f"👤 Name      : {BOLD}{user.first_name}{RESET}")
        print(f"🔗 Username  : @{user.username if user.username else 'None'}")
        print(f"🆔 Bot ID    : {user.id}")
        print(f"✅ Verified  : {user.verified}")
        print(f"🚩 Scam Flag : {RED}{user.scam}{RESET}")

        target_link = None

        if bot_info:
            menu_button = bot_info.menu_button
            if menu_button and isinstance(menu_button, types.BotMenuButton):
                target_link = menu_button.url
                print(f"\n{CYAN}🌐 Website Link Found: {UNDERLINE}{target_link}{RESET}")
            else:
                print(f"\n{YELLOW}⚠️ Menu Link Not Found (Bot might not have a web app).{RESET}")

            if bot_info.commands:
                print(f"\n{BOLD}📜 Available Commands:{RESET}")
                for cmd in bot_info.commands:
                    print(f"   ➤ /{cmd.command} - {cmd.description}")

        print(f"{GREEN}──────────────────────────────{RESET}")

        # Download Option
        if target_link:
            print(f"\n{BOLD}{YELLOW}[?] Do you want to download the website code?{RESET}")
            choice = input(f"Type {GREEN}'yes'{RESET} to download or press Enter to skip: ").lower()
            
            if choice == "yes" or choice == "y":
                custom_name = input(f"📝 Enter file name to save (e.g., index): ")
                if custom_name.strip():
                    download_website(target_link, custom_name)
                else:
                    print(f"{RED}Invalid Name. Cancelled.{RESET}")

    except Exception as e:
        print(f"{RED}[ERROR] {e}{RESET}")

# =============================
# MAIN SYSTEM
# =============================

async def main():
    print_banner()
    
    api_id, api_hash = get_api()

    print(f"\n{CYAN}📱 LOGIN SECTION{RESET}")
    print("──────────────────────────────")
    phone = input("Enter Phone Number (with country code): ")

    client = TelegramClient("lagatech_session", api_id, api_hash)

    await client.connect()

    if not await client.is_user_authorized():
        print(f"\n{CYAN}[*] Sending OTP...{RESET}")
        print(f"{YELLOW}💡 Check your Telegram App for the OTP code (SMS might not work).{RESET}")
        
        try:
            await client.send_code_request(phone)
            code = input("👉 Enter OTP Code: ")
            await client.sign_in(phone, code)
        except SessionPasswordNeededError:
            print(f"{YELLOW}🔐 Two-Step Verification Enabled.{RESET}")
            password = input("👉 Enter 2FA Password: ")
            await client.sign_in(password=password)
        except Exception as e:
            print(f"{RED}Login Failed: {e}{RESET}")
            return

    loading_spin("Logging In", 2)
    print(f"{GREEN}\n✅ Login Successful! Welcome to the System.\n{RESET}")

    while True:
        print(f"\n{BOLD}{CYAN}─── NEW SCAN ───{RESET}")
        bot_username = input("🤖 Enter Bot Username (or type 'exit'): ")

        if bot_username.lower() == "exit":
            print(f"\n{YELLOW}Exiting Tool... Goodbye Hacker! 👋{RESET}")
            break

        await scan_bot(client, bot_username)

# =============================
# RUN
# =============================

if __name__ == "__main__":
    try:
        if sys.platform.startswith('win'):
            # For Windows color support
            os.system('color')
        
        asyncio.run(main())

    except KeyboardInterrupt:
        print(f"\n{RED}Force Closed by User.{RESET}")
