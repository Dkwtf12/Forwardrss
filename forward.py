import logging
from pyrogram import Client, filters
import re
import config
from pyrogram.enums import ParseMode
from flask import Flask
import threading
import sqlite3

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
NYAA_PATTERN = re.compile(r"https?://nyaa\.si/download/\S+\.torrent")
YTS_PATTERN = re.compile(r"https?://yts\.mx/torrent/download/\S+")
TMVCLOUD_PATTERN = re.compile(r"https://cloudserver-1\.tmbcloud\.pro/[A-Z0-9]+")

# SQLite setup
def init_db():
    conn = sqlite3.connect("links.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS processed_links (
            link TEXT PRIMARY KEY
        )
    """)
    conn.commit()
    conn.close()

def is_duplicate_link(link: str) -> bool:
    conn = sqlite3.connect("links.db")
    c = conn.cursor()
    c.execute("SELECT 1 FROM processed_links WHERE link = ?", (link,))
    result = c.fetchone()
    conn.close()
    return result is not None

def save_link(link: str):
    conn = sqlite3.connect("links.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO processed_links (link) VALUES (?)", (link,))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    finally:
        conn.close()

def start_forwarding(app: Client):
    @app.on_message(filters.chat(config.SOURCE_CHAT_ID))
    async def forward_links(client, message):
        try:
            text = message.text or message.caption
            logger.info(f"Received message: {text}")

            if not text:
                logger.warning("Message has no text or caption.")
                return

            links_to_check = {
                "gofile": GOFILE_PATTERN.findall(text),
                "milkie": MILKIE_PATTERN.findall(text),
                "magnet": MAGNET_PATTERN.findall(text),
                "nyaa": NYAA_PATTERN.findall(text),
                "yts": YTS_PATTERN.findall(text),
                "tmvcloud": TMVCLOUD_PATTERN.findall(text),
            }

            if not any(links_to_check.values()):
                logger.info("No matching links found in message.")
                return

            for link_type, links in links_to_check.items():
                for link in links:
                    if is_duplicate_link(link):
                        logger.info(f"Skipping duplicate link from DB: {link}")
                        continue

                    save_link(link)

                    if link_type == "gofile":
                        formatted = f"/l2 {link}\n<b>Tag:</b> <code>@{config.TAG_USERNAME}</code> <code>{config.USER_ID}</code>"
                        await client.send_message(config.DEST_CHAT_ID, formatted, parse_mode=ParseMode.HTML)

                    elif link_type == "milkie":
                        formatted = f"/ql2 {link} -ff metadata\nTag: @{config.TAG_USERNAME} {config.USER_ID}"
                        await client.send_message(config.DEST_CHAT_ID, formatted)

                    elif link_type == "magnet":
                        formatted = f"/ql4 {link} -ff metadata\nTag: @{config.TAG_USERNAME} {config.USER_ID}"
                        await client.send_message(config.DEST_CHAT_ID, formatted)

                    elif link_type == "nyaa":
                        formatted = f"/ql2 {link} -ff metadata\nTag: @{config.TAG_USERNAME} {config.USER_ID}"
                        await client.send_message(config.DEST_CHAT_ID, formatted)

                    elif link_type == "yts":
                        formatted = f"/ql4 {link} -ff metadata\nTag: @{config.TAG_USERNAME} {config.USER_ID}"
                        await client.send_message(config.DEST_CHAT_ID, formatted)

                    elif link_type == "tmvcloud":
                        formatted = f"/ql4 {link} -ff metadata\nTag: @{config.TAG_USERNAME} {config.USER_ID}"
                        await client.send_message(config.DEST_CHAT_ID, formatted)

        except Exception as e:
            logger.exception(f"Error while forwarding links: {e}")

    logger.info("Forwarding setup complete with /l, /ql, and /ql formats.")

# Start the bot
if __name__ == "__main__":
    init_db()
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
