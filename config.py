import os

API_ID = int(os.getenv("API_ID", "19977673"))
API_HASH = os.getenv("API_HASH", "f75386c7aab88e2ad9b5de220fc0ceb4")
BOT_TOKEN = os.getenv("BOT_TOKEN", "5044558270:AAETnUGHgVriS9y_b5ImSC2qOeuRuBLkTp4")

SOURCE_CHAT_ID = int(os.getenv("SOURCE_CHAT_ID", "-1002440398569"))
DEST_CHAT_ID = int(os.getenv("DEST_CHAT_ID", "-1002477240145"))

TAG_USERNAME = os.getenv("TAG_USERNAME", "zsbhere")
USER_ID = int(os.getenv("USER_ID", "1568895149"))

TG_WORKERS = int(os.getenv("TG_WORKERS", "4"))
