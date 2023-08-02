from persiantools.jdatetime import JalaliDate
from datetime import datetime


def getDayOfYear(month, day, dateType="persian"):
    days_in_month = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]
    day_of_year = sum(days_in_month[: month - 1]) + day
    return day_of_year


def jalaliToTimestamp(year, month, day):
    jalilFormat = JalaliDate(year, month, day)
    gregorianDate = JalaliDate.to_gregorian(jalilFormat)
    dateFormat = datetime(gregorianDate.year, gregorianDate.month, gregorianDate.day)
    timestamp = int(datetime.timestamp(dateFormat))
    return timestamp
