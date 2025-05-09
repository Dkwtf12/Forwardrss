import logging import re from pyrogram import Client, filters from pyrogram.enums import ParseMode from pyrogram.types import Message from config import SOURCE_CHAT_ID, DEST_CHAT_ID, USER_ID

Enable logging

logging.basicConfig(level=logging.INFO) logger = logging.getLogger(name)

Initialize the userbot client

userbot = Client( name="userbot", api_id=int(os.environ["API_ID"]), api_hash=os.environ["API_HASH"], session_string=os.environ["SESSION_STRING"] )

Regex pattern to match links

LINK_PATTERN = re.compile(r"https?://t.me/\S+")

@userbot.on_message(filters.chat(SOURCE_CHAT_ID)) async def forward_links(_, message: Message): if message.text: links = LINK_PATTERN.findall(message.text) if links: try: await userbot.send_message( chat_id=DEST_CHAT_ID, text=message.text, parse_mode=ParseMode.HTML ) logger.info(f"Forwarded message with links: {links}") except Exception as e: logger.error(f"Failed to forward message: {e}")

if name == "main": logger.info("Starting userbot...") userbot.run()

