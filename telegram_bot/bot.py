import os
from pathlib import Path

import requests
from dotenv import load_dotenv

# Load this package's own .env regardless of the current working directory.
load_dotenv(Path(__file__).resolve().parent / ".env")


class TelegramBot:

    def __init__(
            self,
            bot_token: str | None = None,
            chat_ids: list[str] | None = None,
    ) -> None:
        bot_token = bot_token or os.getenv("BOT_TOKEN")
        if chat_ids is None:
            chat_id = os.getenv("CHAT_ID_1")
            chat_ids = [chat_id] if chat_id else []

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

