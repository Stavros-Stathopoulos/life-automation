"""Allows `python -m nameday_reminder` to print today's reminder."""

from . import NamedayReminder

message = NamedayReminder().build_message()
print(message or "Failed to retrieve nameday information.")
