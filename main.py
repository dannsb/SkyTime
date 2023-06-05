from skyobjects.moon import moon
from skyobjects.sun import sun
from datetime import date
from persiantools.jdatetime import JalaliDate
from os import system

def printBanner():
    system("cls")
    with open('banner.txt', 'r') as f:
        for line in f:
            print(line.rstrip())
printBanner()

inputDate = input("\nPlease enter your date (leave it empty for today) : ")
if not inputDate:
    inputDate = JalaliDate.today().strftime("%Y/%m/%d")

def calcDayOfYear(date,dateType="persian"):
    month = int(date.split("/")[1])
    day = int(date.split("/")[2])
    dayOfYear = 0
    counter = 1
    while counter<month:
        if(counter <=6):
            dayOfYear += 31
        else:
            dayOfYear += 30
        counter += 1
    dayOfYear = dayOfYear + day
    return dayOfYear

sun.dayLength(calcDayOfYear(inputDate))
