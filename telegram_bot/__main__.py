"""Allows `python -m telegram_bot` to send a test message."""

from . import TelegramBot

TelegramBot().send_message("Hello from the Telegram Bot!")
