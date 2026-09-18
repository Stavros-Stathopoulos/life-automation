"""Greek nameday reminder package.

Public API:
    get_nameday     - fetch the namedays for a given date from the greek-eortologio API.
    NamedayReminder - builds a human-readable reminder message for today's namedays.
"""

from .nameday import get_nameday
from .reminder import NamedayReminder

__all__ = ["get_nameday", "NamedayReminder"]
