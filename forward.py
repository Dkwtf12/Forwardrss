from pyrogram import Client, filters
import re
import config
from pyrogram.enums import ParseMode
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

# Run Flask in a separate thread
threading.Thread(target=run_flask, daemon=True).start()

# Regex patterns
GOFILE_PATTERN = re.compile(r"https?://(?:www\.)?gofile\.io/\S+")
MILKIE_PATTERN = re.compile(r"https?://milkie\.cc/api/v1/torrents/\S+")
MAGNET_PATTERN = re.compile(r"magnet:\?xt=urn:btih:[a-zA-Z0-9]+")

def start_forwarding(app: Client):
    @app.on_message(filters.chat(config.SOURCE_CHAT_ID))
    async def forward_links(client, message):
        text = message.text or message.caption
        if not text:
            return

        gofile_links = GOFILE_PATTERN.findall(text)
        milkie_links = MILKIE_PATTERN.findall(text)
        magnet_links = MAGNET_PATTERN.findall(text)

        for link in gofile_links:
            formatted = f"/l {link}\n<b>Tag:</b> <code>@{config.TAG_USERNAME}</code> <code>{config.USER_ID}</code>"
            await client.send_message(config.DEST_CHAT_ID, formatted, parse_mode=ParseMode.HTML)

        for link in milkie_links:
            formatted = f"/ql3 {link} -ff metadata -up {config.DEST_CHAT_ID}\nTag: @{config.TAG_USERNAME} {config.USER_ID}"
            await client.send_message(config.DEST_CHAT_ID, formatted)

        for link in magnet_links:
            formatted = f"/ql2 {link} -ff metadata -up {config.DEST_CHAT_ID}\nTag: @{config.TAG_USERNAME} {config.USER_ID}"
            await client.send_message(config.DEST_CHAT_ID, formatted)

    print("Forwarding setup complete with /l, /ql3, and /ql2 formats.")
