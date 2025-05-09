from pyrogram import Client
import config
from forward import start_forwarding

app_1 = Client(
    "AutoForwardBot1",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN_1,  # Using BOT_TOKEN_1 here
    workers=config.TG_WORKERS
)

app_2 = Client(
    "AutoForwardBot2",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN_2,  # Using BOT_TOKEN_2 here
    workers=config.TG_WORKERS
)

if __name__ == "__main__":
    print("Bot is running...")
    start_forwarding(app_1)  # Forwarding links for Bot 1
    start_forwarding(app_2)  # Forwarding links for Bot 2 (or you can call start_bot_2 depending on your needs)
    
    app_1.run()  # Run Bot 1
    app_2.run()  # Run Bot 2
