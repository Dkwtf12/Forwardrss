import os

# Telegram API credentials
API_ID = int(os.environ["19977673"])
API_HASH = os.environ["f75386c7aab88e2ad9b5de220fc0ceb4"]

# Bot token for the forwarding bot
BOT_TOKEN_1 = os.environ.get("5044558270:AAETnUGHgVriS9y_b5ImSC2qOeuRuBLkTp4")

# Session string for the userbot (exported from Pyrogram)
SESSION_STRING = os.environ.get("BQEw1ckAjbK5gm36s2Qs93i6XjLu9jZmbSGMV062W9Ddtd_A_vVhgjgJrpXzaqqDGiT5aBVi22SVbxMyVrFBaMyc6n7479OXUPwaywVL0PkRnqvgAhXRvnZ7fk6pdxktOCyRT-kGnb_GpU0wdZU3Sb_zBQKDx2Vj89o44u5N2j_J-EK0sLLscCKvalN4UXRkA-IYqjhI5i5b1EFiPPZFnDcJurNZknU4UHhvlc3GYj0gcgHQpC6xIWJbbi_RWHPYISz8eQZnZqGdpfYXYiZNzqSffP6l5ZB1Lko0nXegov7dNgCoHvG2Ud2vp2QDtFZGXjC-aaHIFsjqv9pPPVCWkcHkNhoyAwAAAAGnwwoiAA")


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
