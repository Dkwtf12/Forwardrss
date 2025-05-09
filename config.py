import asyncio
import logging
from pyrogram import idle
from forward import bot_1, userbot

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    logger.info("Starting Telegram clients (bot and userbot)...")
    await bot_1.start()
    await userbot.start()

    await idle()

    await bot_1.stop()
    await userbot.stop()
    logger.info("Telegram clients stopped.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.error(f"Error in main(): {e}")
