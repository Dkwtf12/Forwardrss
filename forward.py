import logging
from pyrogram import Client, filters
import re
import config
from pyrogram.enums import ParseMode
from flask import Flask
import threading

# Setup logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Flask app for Heroku uptime ping
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

# Start Flask in background
threading.Thread(target=run_flask, daemon=True).start()

# Regex patterns
GOFILE_PATTERN = re.compile(r"https?://(?:www\.)?gofile\.io/\S+")
MILKIE_PATTERN = re.compile(r"https?://milkie\.cc/api/v1/torrents/\S+")
MAGNET_PATTERN = re.compile(r"magnet:\?xt=urn:btih:[a-zA-Z0-9]+[^\s]*")

def start_forwarding(app: Client):
    @app.on_message(filters.chat(config.SOURCE_CHAT_ID))
    async def forward_links(client, message):
        try:
            text = message.text or message.caption
            logger.info(f"Received message: {text}")

            if not text:
                logger.warning("Message has no text or caption.")
                return

            gofile_links = GOFILE_PATTERN.findall(text)
            milkie_links = MILKIE_PATTERN.findall(text)
            magnet_links = MAGNET_PATTERN.findall(text)

            if not (gofile_links or milkie_links or magnet_links):
                logger.info("No matching links found in message.")
                return

            for link in gofile_links:
                formatted = f"/l {link}\n<b>Tag:</b> <code>@{config.TAG_USERNAME}</code> <code>{config.USER_ID}</code>"
                logger.info(f"Sending Gofile link: {formatted}")
                await client.send_message(config.DEST_CHAT_ID, formatted, parse_mode=ParseMode.HTML)

            for link in milkie_links:
                formatted = f"/ql3 {link} -ff metadata\nTag: @{config.TAG_USERNAME} {config.USER_ID}"
                logger.info(f"Sending Milkie link: {formatted}")
                await client.send_message(config.DEST_CHAT_ID, formatted)

            for link in magnet_links:
                formatted = f"/ql2 {link} -ff metadata\nTag: @{config.TAG_USERNAME} {config.USER_ID}"
                logger.info(f"Sending Magnet link: {formatted}")
                await client.send_message(config.DEST_CHAT_ID, formatted)

        except Exception as e:
            logger.exception(f"Error while forwarding links: {e}")

    logger.info("Forwarding setup complete with /l, /ql3, and /ql2 formats.")

def start_bot_2(app: Client):
    @app.on_message(filters.chat(config.DEST_CHAT_ID))
    async def copy_and_paste_to_group(client, message):
        try:
            text = message.text or message.caption
            logger.info(f"Received message from destination channel: {text}")

            if not text:
                logger.warning("Message has no text or caption.")
                return

            # Forward message to group (TARGET_GROUP_ID)
            await client.send_message(config.TARGET_GROUP_ID, text)
            logger.info(f"Message copied and pasted to the group: {text}")

        except Exception as e:
            logger.exception(f"Error occurred while copying and pasting message to group: {e}")

    logger.info("Bot 2 setup complete for copying and pasting messages.")

# Instantiate bots for later use
bot_1 = Client(
    "bot_1",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN_1,
    workers=config.TG_WORKERS
)

bot_2 = Client(
    "bot_2",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN_2,
    workers=config.TG_WORKERS
)

# Start both bots
start_forwarding(bot_1)  # Bot 1: Forwarding links to the destination channel
start_bot_2(bot_2)      # Bot 2: Copy and paste to the group

# Run both bots explicitly
bot_1.run()  # Ensure bot 1 is running
bot_2.run()  # Ensure bot 2 is running

logger.info("Both bots started and running.")
