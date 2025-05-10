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
logger = logging.getLogger(name)

# Flask app for Heroku uptime ping
app = Flask(name)

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
                formatted = f"/ql {link} -ff metadata\nTag: @{config.TAG_USERNAME} {config.USER_ID}"
                logger.info(f"Sending Milkie link: {formatted}")
                await client.send_message(config.DEST_CHAT_ID, formatted)

            for link in magnet_links:
                formatted = f"/ql {link} -ff metadata\nTag: @{config.TAG_USERNAME} {config.USER_ID}"
                logger.info(f"Sending Magnet link: {formatted}")
                await client.send_message(config.DEST_CHAT_ID, formatted)

        except Exception as e:
            logger.exception(f"Error while forwarding links: {e}")

    logger.info("Forwarding setup complete with /l, /ql, and /ql formats.")

# Start the bot
if name == "main":
    bot = Client(
        "bot",
        api_id=config.API_ID,
        api_hash=config.API_HASH,
        bot_token=config.BOT_TOKEN,
        workers=config.TG_WORKERS
    )

    start_forwarding(bot)
    logger.info("Starting bot...")
    bot.run()
