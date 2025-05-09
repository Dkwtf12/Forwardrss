import asyncio
from forward import bot_1, userbot

async def main():
    await asyncio.gather(bot_1.start(), userbot.start())
    print("Both bots started.")
    await asyncio.Event().wait()  # Keeps the script alive

if __name__ == "__main__":
    asyncio.run(main())
