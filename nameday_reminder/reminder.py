import time

from .nameday import get_nameday


class NamedayReminder:
    """Builds a reminder message for the namedays of a given day (default: today)."""

    def __init__(self, day: int | None = None, month: int | None = None, year: int | None = None) -> None:
        now = time.localtime()
        self.day = day or now.tm_mday
        self.month = month or now.tm_mon
        self.year = year or now.tm_year

    def build_message(self) -> str | None:
        """Return a formatted message, or None if the API returned nothing."""
        info = get_nameday(self.day, self.month, self.year)
        if not info:
            return None
        return self.format(info, f"{self.day}/{self.month}/{self.year}")

    @staticmethod
    def format(info: dict, date: str) -> str:
        """Format a greek-eortologio API response.

        Expected keys: dayName, dayWhat, names (comma-separated string), worldDay.
        """
        header = f"Namedays for\n"
        if info.get("dayName"):
            header += f"{info['dayName']}, {date}"
        lines = [header]

        names = info.get("names")
        if names:
            lines.append("")
            lines.append("Celebrating today:")
            lines.extend(f"- {name.strip()}" for name in str(names).split(",") if name.strip())

        if info.get("dayWhat"):
            lines.append("")
            lines.append(f"Feast: {info['dayWhat']}")
            lines.append("")
        if info.get("worldDay"):
            lines.append(f"World day: {info['worldDay']}")
            lines.append("")

        return "\n".join(lines)
