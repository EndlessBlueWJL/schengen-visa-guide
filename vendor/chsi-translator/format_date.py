"""Format report dates and derive the configured one-calendar-year expiry."""
from calendar import monthrange
from datetime import datetime


def format_date(date: str) -> str:
    return datetime.strptime(date, "%Y/%m/%d").strftime("%b. %d, %Y")


def get_renewal_date(date: str) -> str:
    return format_date(date)


def get_expiry_date(renewal_date: str) -> str:
    """Return next year's anniversary; February 29 becomes February 28.

    This is the tool's display rule, not a change to CHSI verification validity.
    """
    renewal = datetime.strptime(renewal_date, "%Y/%m/%d")
    year = renewal.year + 1
    day = min(renewal.day, monthrange(year, renewal.month)[1])
    return renewal.replace(year=year, day=day).strftime("%b. %d, %Y")
