#!/usr/bin/env python3
# ============================================
# TELEGRAM BOT SCANNER - ULTRA HACKER EDITION
# Dev: @lagatech
# ============================================

import asyncio
import os
import time
from telethon import TelegramClient, functions, types
from telethon.errors import SessionPasswordNeededError

# =============================
# Colors
# =============================

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# =============================
# Hacker Logo
# =============================

logo = f"""{GREEN}

██╗      █████╗  ██████╗  █████╗ ████████╗███████╗ ██████╗██╗  ██╗
██║     ██╔══██╗██╔════╝ ██╔══██╗╚══██╔══╝██╔════╝██╔════╝██║  ██║
██║     ███████║██║  ███╗███████║   ██║   █████╗  ██║     ███████║
██║     ██╔══██║██║   ██║██╔══██║   ██║   ██╔══╝  ██║     ██╔══██║
███████╗██║  ██║╚██████╔╝██║  ██║   ██║   ███████╗╚██████╗██║  ██║
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝

        TELEGRAM BOT SCANNER
          ULTRA EDITION

        DEV : @lagatech

{RESET}
"""

# =============================
# Animation
# =============================

def loading(text="Scanning"):
    for i in range(3):
        print(f"{CYAN}{text}{'.'*i}{RESET}", end="\r")
        time.sleep(0.5)

# =============================
# API System
# =============================

def get_api():

    if os.path.exists("config.txt"):
        with open("config.txt") as f:
            api_id = f.readline().strip()
            api_hash = f.readline().strip()

    else:

        print(YELLOW+"\nEnter Telegram API Credentials\n"+RESET)

        api_id = input("API ID : ")
        api_hash = input("API HASH : ")

        with open("config.txt","w") as f:
            f.write(api_id+"\n")
            f.write(api_hash+"\n")

    return api_id, api_hash


# =============================
# Bot Scanner
# =============================

async def scan_bot(client, bot_username):

    try:

        loading()

        bot = await client.get_entity(bot_username)

        result = await client(functions.users.GetFullUserRequest(id=bot))

        user = result.users[0]
        bot_info = result.full_user.bot_info

        print(f"\n{GREEN}========== BOT INFO =========={RESET}")

        print("Name      :", user.first_name)
        print("Username  :", "@"+user.username if user.username else "None")
        print("Bot ID    :", user.id)
        print("Verified  :", user.verified)
        print("Scam Flag :", user.scam)

        if bot_info:

            menu_button = bot_info.menu_button

            if menu_button and isinstance(menu_button, types.BotMenuButton):
                print(f"\n🔗 Menu Link : {menu_button.url}")

            else:
                print("\nMenu Link : Not Found")

            if bot_info.commands:
                print("\n📜 Commands :")

                for cmd in bot_info.commands:
                    print(f" /{cmd.command} - {cmd.description}")

        print(f"{GREEN}===============================\n{RESET}")

    except Exception as e:

        print(f"{RED}[ERROR] {e}{RESET}")


# =============================
# MAIN SYSTEM
# =============================

async def main():

    os.system("clear")
    print(logo)

    api_id, api_hash = get_api()

    phone = input("📱 Enter Phone Number : ")

    client = TelegramClient("lagatech_session", api_id, api_hash)

    await client.connect()

    if not await client.is_user_authorized():

        print("\nSending OTP...")
        await client.send_code_request(phone)

        code = input("Enter OTP : ")

        try:
            await client.sign_in(phone, code)

        except SessionPasswordNeededError:
            password = input("Two Step Password : ")
            await client.sign_in(password=password)

    print(GREEN+"\nLogin Successful\n"+RESET)

    while True:

        bot_username = input("🤖 Enter Bot Username : ")

        if bot_username.lower() == "exit":
            break

        await scan_bot(client, bot_username)


# =============================
# RUN
# =============================

if __name__ == "__main__":

    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        print("\nTool Closed")
