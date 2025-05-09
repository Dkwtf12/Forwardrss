
import logging
from pyrogram import Client, filters
from config import API_ID, API_HASH, SESSION_STRING, DEST_CHAT_ID, TARGET_GROUP_ID, TG_WORKERS

# Initialize logging for this module
logger = logging.getLogger(__name__)

# Create the userbot client with a session string
userbot = Client(
    "user_forwarder",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
    workers=TG_WORKERS
)

@userbot.on_message(filters.chat(DEST_CHAT_ID))
async def copy_to_group(client, message):
    """
    Handler for new messages in DEST_CHAT_ID.
    Copies the message content to TARGET_GROUP_ID as a normal message (no forward tag).
    """
    try:
        # Copy the message to the target group
        await client.copy_message(
            chat_id=TARGET_GROUP_ID,
            from_chat_id=message.chat.id,
            message_id=message.message_id
        )
        logger.info(f"Copied message {message.message_id} from {DEST_CHAT_ID} to {TARGET_GROUP_ID}")
    except Exception as e:
        logger.error(f"Failed to copy message to TARGET_GROUP_ID: {e}")
