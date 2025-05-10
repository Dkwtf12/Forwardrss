from pyrogram import Client
import config
from forward import start_forwarding

app = Client(
    "AutoForwardBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    workers=config.TG_WORKERS
)

if __name__ == "__main__":
    print("Bot is running...")
    start_forwarding(app)
    app.run()
