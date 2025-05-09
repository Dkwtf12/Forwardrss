
import re
import logging
from pyrogram import idle
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN_1, SOURCE_CHAT_ID, DEST_CHAT_ID, TAG_USERNAME, USER_ID, TG_WORKERS

# Initialize logging for this module
logger = logging.getLogger(__name__)

# Define regex patterns for different link types
GOFILE_REGEX = re.compile(r'https?://(?:www\.)?gofile\.\S+', re.IGNORECASE)
MILKIE_REGEX = re.compile(r'https?://(?:www\.)?milkie\.\S+', re.IGNORECASE)
MAGNET_REGEX = re.compile(r'magnet:\?xt=urn:[^\s]+', re.IGNORECASE)

# Create the bot client
bot = Client(
    "bot_forwarder",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN_1,
    workers=TG_WORKERS
)

@bot.on_message(filters.chat(SOURCE_CHAT_ID))
async def forward_links(client, message):
    """
    Handler for new messages in SOURCE_CHAT_ID.
    Finds Gofile, Milkie, or Magnet links in the message text/caption.
    If found, formats and forwards them to DEST_CHAT_ID.
    """
    text = message.text or message.caption or ""
    if not text:
        return  # Nothing to process

    # Find all matching links
    gofile_links = GOFILE_REGEX.findall(text)
    milkie_links = MILKIE_REGEX.findall(text)
    magnet_links = MAGNET_REGEX.findall(text)

    # If no relevant links are found, do nothing
    if not (gofile_links or milkie_links or magnet_links):
        return

    # Build the formatted message
    lines = []
    # Optionally add a header or mention
    mention = ""
    if USER_ID and TAG_USERNAME:
        # Mention by ID (keeps clickable even if username changes)
        mention = f'<a href="tg://user?id={USER_ID}">{TAG_USERNAME}</a>'
    elif TAG_USERNAME:
        mention = f"@{TAG_USERNAME}"

    if mention:
        lines.append(f"🔔 <b>New links posted by {mention}:</b>\n")

    # Add each found link with a label
    for link in gofile_links:
        lines.append(f"📁 <b>Gofile Link:</b> {link}")
    for link in milkie_links:
        lines.append(f"🎞️ <b>Milkie Link:</b> {link}")
    for link in magnet_links:
        lines.append(f"🧲 <b>Magnet Link:</b> {link}")

    formatted_text = "\n".join(lines)

    # Send the formatted message to the destination channel
    try:
        await client.send_message(
            DEST_CHAT_ID,
            formatted_text,
            parse_mode="HTML",
            disable_web_page_preview=True
        )
        logger.info(f"Forwarded links to DEST_CHAT_ID: {formatted_text}")
    except Exception as e:
        logger.error(f"Failed to send message to DEST_CHAT_ID: {e}")
