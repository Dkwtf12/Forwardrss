import os

# Telegram API credentials
API_ID = os.environ.get("19977673")
API_HASH = os.environ.get("f75386c7aab88e2ad9b5de220fc0ceb4")

# Bot token for the forwarding bot
BOT_TOKEN_1 = os.environ.get("5044558270:AAETnUGHgVriS9y_b5ImSC2qOeuRuBLkTp4")

# Session string for the userbot (exported from Pyrogram)
SESSION_STRING = os.environ.get("1BVtsOMQBuwYQZwy0vUwa8fBStV8VW6muYLqSR3egK8UGBWhJc1MoGTqWgOYxlA8zKvBu71QNFdL0Zqr98OmdLMyxDHvblyIQYBk9ubR7xJHJXjSdL8RgO__hi1TquqArpCWyVk2YcLWbF-mJXur_9jh5o3Dn_F6hWT7bCw4usPDXActluxyZQuymiWfZvsT6pnLTRYjfaMv6fWgQkebMd6Bpc7eXNo7oFrXVJund06MR8cLqVa6KHws-SA5Gvli9CPi9xO2O4aNrXJhZ5dNSTJ9xwAX-HlWpvq31OZ4h4t9048szjXahps0Pbp8BnQVLgSCQ-ssoDUGsM1vV__840Rq_LywFR70=")


# Chat IDs (use integers). SOURCE_CHAT_ID is the channel to watch, DEST_CHAT_ID is where bot will send.
SOURCE_CHAT_ID = int(os.environ.get("SOURCE_CHAT_ID", "-1002615357378"))
DEST_CHAT_ID = int(os.environ.get("DEST_CHAT_ID", "-1002477240145"))

# Group ID for the userbot to forward messages to.
TARGET_GROUP_ID = int(os.environ.get("TARGET_GROUP_ID", "-1002356176128"))

# (Optional) Tagging: username and user ID to mention in forwarded messages
TAG_USERNAME = os.environ.get("TAG_USERNAME")  # e.g. "@zsbhere"
USER_ID = int(os.environ.get("USER_ID", 0)) if os.environ.get("1568895149") else None

# Pyrogram workers (concurrency for handling updates)
TG_WORKERS = int(os.environ.get("TG_WORKERS", 4))
