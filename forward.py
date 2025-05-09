import logging
import re
import config
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from flask import Flask
import threading

# Logging setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Flask app for uptime ping
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

threading.Thread(target=run_flask, daemon=True).start()

# Regex patterns
GOFILE_PATTERN = re.compile(r"https?://(?:www\.)?gofile\.io/\S+")
MILKIE_PATTERN = re.compile(r"https?://milkie\.cc/api/v1/torrents/\S+")
MAGNET_PATTERN = re.compile(r"magnet:\?xt=urn:btih:[a-zA-Z0-9]+[^\s]*")

# Clients
bot_1 = Client(
    "bot1",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN_1
)

userbot = Client(
    "userbot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=config.SESSION_STRING
)

# Bot 1 forwards from source to destination
@bot_1.on_message(filters.chat(config.SOURCE_CHAT_ID))
async def forward_links(client, message):
    text = message.text or message.caption
    if not text:
        return

    gofile_links = GOFILE_PATTERN.findall(text)
    milkie_links = MILKIE_PATTERN.findall(text)
    magnet_links = MAGNET_PATTERN.findall(text)

    if not (gofile_links or milkie_links or magnet_links):
        return

    for link in gofile_links:
        formatted = f"/l {link}\n<b>Tag:</b> <code>@{config.TAG_USERNAME}</code> <code>{config.USER_ID}</code>"
        await client.send_message(config.DEST_CHAT_ID, formatted, parse_mode=ParseMode.HTML)

    for link in milkie_links:
        formatted = f"/ql3 {link} -ff metadata\nTag: @{config.TAG_USERNAME} {config.USER_ID}"
        await client.send_message(config.DEST_CHAT_ID, formatted)

    for link in magnet_links:
        formatted = f"/ql2 {link} -ff metadata\nTag: @{config.TAG_USERNAME} {config.USER_ID}"
        await client.send_message(config.DEST_CHAT_ID, formatted)

# Userbot reads from DEST_CHAT_ID and posts to group
@userbot.on_message(filters.chat(config.DEST_CHAT_ID))
async def copy_to_group(client, message):
    text = message.text or message.caption
    if text:
        await client.send_message(config.TARGET_GROUP_ID, text)

# Run both clients together
async def main():
    await asyncio.gather(
        bot_1.start(),
        userbot.start()
    )
    print("Both bot_1 and userbot started")

    await asyncio.Event().wait()  # Keeps it running

if __name__ == "__main__":
    asyncio.run(main())
