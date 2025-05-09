import os

# Telegram API credentials
API_ID = os.environ.get("28737520")
API_HASH = os.environ.get("c23aef82a6c369b5791cf0529d3fc090")

# Bot token for the forwarding bot
BOT_TOKEN_1 = os.environ.get("5044558270:AAETnUGHgVriS9y_b5ImSCqOeuRuBLkTp4")
# Session string for the userbot (exprte from Pyrogram)
SESSION_STRING = os.environ.get("BQG2f_AAonTtp3hsBwMPAbyPuazoZT_86fa5w3eYdovrxGfa5OhrNWxFg9JAIevW4WwVX__InfWMr9krySUOfHQHxvDxHmGBAE5X1qZj7O1NnK_0rpSUGJTFTJitrU0vjG2ogek0ROp1EN9JPktlpY-5JCySoehJbMwolTe0IMY4hU58Kcd6vC9HLUbLv8cNfXAi-SbVZVls2Jt_RsHBIFElTAGYfdnNEmRSIsaJuWsTwmq3bXNuhsqHNntaPl2naP7b3Z88qZspBfN0KzCNVpSz3OsdUvo-_1YCJpygjW6-qefTeeykbrPE-tLGnN5vc0FqG_NbsKJ8Mbds7EupWBxWyV1Y0AAAAAGnwwoiAA")


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
