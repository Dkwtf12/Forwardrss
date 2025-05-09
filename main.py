import asyncio
import logging
import threading
from flask import Flask
from pyrogram import compose
from bot import bot      # Import the bot client from bot.py
from userbot import userbot  # Import the userbot client

# Configure root logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def run_flask():
    """
    Starts a simple Flask server for uptime pings.
    """
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Bot is running."

    # Use port from environment or default 5000
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    # Start Flask server in a separate daemon thread
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    logger.info("Flask web server started for uptime ping.")

    # Run both Pyrogram clients concurrently
    logger.info("Starting Telegram clients (bot and userbot)...")
    try:
        asyncio.run(compose([bot, userbot]))
    except Exception as e:
        logger.error(f"Error in compose(): {e}")
