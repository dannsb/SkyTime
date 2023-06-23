from skyobjects.moon import moon
from skyobjects.sun import sun
from datetime import datetime
from persiantools.jdatetime import JalaliDate
from progress.spinner import MoonSpinner
from os import system
import threading
from time import sleep


def printBanner():
    system("cls")
    with open("banner.txt", "r") as f:
        for line in f:
            print(line.rstrip())


def calcDayOfYear(month, day, dateType="persian"):
    dayOfYear = 0
    counter = 1
    while counter < month:
        if counter <= 6:
            dayOfYear += 31
        else:
            dayOfYear += 30
        counter += 1
    dayOfYear = dayOfYear + day
    return dayOfYear


def jalilToTimestamp(year, month, day):
    jalilFormat = JalaliDate(year, month, day)
    gregorianDate = JalaliDate.to_gregorian(jalilFormat)
    dateFormat = datetime(gregorianDate.year, gregorianDate.month, gregorianDate.day)
    timestamp = int(datetime.timestamp(dateFormat))
    return timestamp


def calDatas():
    global lunarDate, sunRiseTime, sunSetTime
    year = int(splitedDate[0])
    month = int(splitedDate[1])
    day = int(splitedDate[2])
    timestamp = jalilToTimestamp(year, month, day)
    lunarDate = moon.getLunarDay(timestamp)
    dayLength = sun.dayLength(calcDayOfYear(month, day), 30)
    sunRiseTime = sun.sunRise(dayLength)
    sunSetTime = sun.sunSet(dayLength, sunRiseTime)


try:
    printBanner()
    today = JalaliDate.today().strftime("%Y/%m/%d")
    userDate = input(f"\nPlease enter your date [{today}] : ")
    if not userDate:
        userDate = today
    splitedDate = userDate.split("/")

    spinner = MoonSpinner("Loading ")

    thread = threading.Thread(target=calDatas)
    thread.start()
    while thread.is_alive():
        spinner.next()
        sleep(0.06)
    thread.join()

    print(
        f"""\n
    date : {userDate}
    lunar date : {lunarDate}
    sun rise : {sunRiseTime}
    sun set : {sunSetTime}
    """
    )

except KeyboardInterrupt:
    exit()

except Exception as err:
    print(err)
