"""Telegram bot package.

Public API:
    TelegramBot - sends text messages to one or more chats via the Telegram Bot API.
"""

from .bot import TelegramBot

__all__ = ["TelegramBot"]
