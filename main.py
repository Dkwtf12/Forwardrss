from forward import bot_1, userbot  # Import bot_1 (for forwarding) and userbot (for copying messages)

if __name__ == "__main__":
    print("Bot is running...")
    bot_1.run()  # Run Bot 1 for forwarding
    userbot.run()  # Run Userbot for copying and pasting messages to the group
