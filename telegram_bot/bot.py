import os
from dotenv import load_dotenv
import requests

load_dotenv()

class TelegramBot:

    def __init__(
            self,
            bot_token: str | None = os.getenv("BOT_TOKEN"),
            chat_ids: list = [os.getenv("CHAT_ID_1")],
    )-> None:
        if not bot_token:
            raise ValueError("Bot token is required.")
        if not chat_ids or not isinstance(chat_ids, list):
            raise ValueError("At least one chat ID is required and must be a list.")
        
        self.bot_token = bot_token
        self.chat_ids = chat_ids
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}/"

    def send_message(self, message: str) -> None:
        for chat_id in self.chat_ids:
            url = f"{self.base_url}sendMessage"
            payload = {
                "chat_id": chat_id,
                "text": message
            }
            response = requests.post(url, json=payload)
            if response.status_code != 200:
                print(f"Failed to send message to chat ID {chat_id}: {response.text}")

if __name__ == "__main__":
    bot = TelegramBot()
    bot.send_message("Hello from the Telegram Bot!")