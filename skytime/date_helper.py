from persiantools.jdatetime import JalaliDate
from datetime import datetime
from ummalqura.hijri_date import HijriDate


def getDayOfYear(month, day, dateType="persian"):
    days_in_month = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]
    day_of_year = sum(days_in_month[: month - 1]) + day
    return day_of_year


def jalaliToGregorian(year, month, day):
    return JalaliDate(year, month, day).to_gregorian()


def gregorianToLunarDay(year,month,day):
    lunarDate = HijriDate(year, month, day, gr=True)
    lunarDate = (
        str(lunarDate.year) + "/" + str(lunarDate.month) + "/" + str(lunarDate.day)
    )
    return lunarDate
