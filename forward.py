import logging
import re
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message
from config import SOURCE_CHAT_ID, DEST_CHAT_ID, USER_ID

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Userbot
userbot = Client(
    "userbot",
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
    in_memory=True
)

# Bot
bot_1 = Client(
    "bot_1",
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
    bot_token=os.environ["BOT_TOKEN_1"],
    in_memory=True
)

# Regex pattern to detect specific link types
link_pattern = re.compile(r"(https?://t\.me/\S+|https?://telegram\.me/\S+)", re.IGNORECASE)

@userbot.on_message(filters.chat(SOURCE_CHAT_ID) & filters.text)
async def catch_and_forward(client: Client, message: Message):
    # If a link is found, forward the message via bot
    if link_pattern.search(message.text):
        try:
            await bot_1.send_message(
                chat_id=DEST_CHAT_ID,
                text=message.text,
                parse_mode=ParseMode.HTML
            )
            logger.info(f"Forwarded message from {SOURCE_CHAT_ID} to {DEST_CHAT_ID}")
        except Exception as e:
            logger.error(f"Failed to forward message: {e}")
