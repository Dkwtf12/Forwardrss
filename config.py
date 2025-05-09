import os

# Telegram API Credentials
API_ID = int(os.getenv("API_ID", "19977673"))
API_HASH = os.getenv("API_HASH", "f75386c7aab88e2ad9b5de220fc0ceb4")

# Bot Tokens (Bot 1 and Bot 2)
BOT_TOKEN_1 = os.getenv("BOT_TOKEN_1", "5044558270:AAETnUGHgVriS9y_b5ImSC2qOeuRuBLkTp4")
BOT_TOKEN_2 = os.getenv("BOT_TOKEN_2", "6049919532:AAEtZF-PMJ4BMZudwDxdmrwWRUq_s2w2ZkY")

# Chat and Group IDs
SOURCE_CHAT_ID = int(os.getenv("SOURCE_CHAT_ID", "-1002615357378"))
DEST_CHAT_ID = int(os.getenv("DEST_CHAT_ID", "-1002477240145"))
TARGET_GROUP_ID = int(os.getenv("TARGET_GROUP_ID", "-1002356176128"))

# User info
TAG_USERNAME = os.getenv("TAG_USERNAME", "zsbhere")
USER_ID = int(os.getenv("USER_ID", "1568895149"))

# Worker Settings (Number of concurrent workers)
TG_WORKERS = int(os.getenv("TG_WORKERS", "4"))

# Session string for userbot (if needed, for your user account)
SESSION_STRING = os.getenv("SESSION_STRING", "BQEw1ckAjbK5gm36s2Qs93i6XjLu9jZmbSGMV062W9Ddtd_A_vVhgjgJrpXzaqqDGiT5aBVi22SVbxMyVrFBaMyc6n7479OXUPwaywVL0PkRnqvgAhXRvnZ7fk6pdxktOCyRT-kGnb_GpU0wdZU3Sb_zBQKDx2Vj89o44u5N2j_J-EK0sLLscCKvalN4UXRkA-IYqjhI5i5b1EFiPPZFnDcJurNZknU4UHhvlc3GYj0gcgHQpC6xIWJbbi_RWHPYISz8eQZnZqGdpfYXYiZNzqSffP6l5ZB1Lko0nXegov7dNgCoHvG2Ud2vp2QDtFZGXjC-aaHIFsjqv9pPPVCWkcHkNhoyAwAAAAGnwwoiAA")
