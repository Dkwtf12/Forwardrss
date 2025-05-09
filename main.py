from forward import bot_1, bot_2, start_forwarding, start_bot_2
from pyrogram import idle
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    start_forwarding(bot_1)
    start_bot_2(bot_2)

    bot_1.start()
    bot_2.start()

    logger.info("Both bots started and running.")
    idle()

    bot_1.stop()
    bot_2.stop()
