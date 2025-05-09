import asyncio
from pyrogram import idle
from forward import bot_1, userbot

async def main():
    await bot_1.start()
    await userbot.start()
    print("Both bots started.")

    # Keep the program running
    await idle()

    # Optional: Stop clients gracefully on shutdown
    await bot_1.stop()
    await userbot.stop()

if __name__ == "__main__":
    asyncio.run(main())
