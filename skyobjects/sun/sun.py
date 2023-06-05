import math


def sunSet(dayLength, sunRiseTime):
    sunSetTime = sunRiseTime + dayLength
    return round(sunSetTime, 2)


def sunRise(dayLength):
    sunRiseTime = 12 - (dayLength / 2)
    return round(sunRiseTime, 2)


def dayLength(dayOfYear, latitude):
    st1 = math.sin(math.radians(dayOfYear * 360 / 365))
    st2 = -math.tan(math.radians(23.5 * st1))
    st3 = math.tan(math.radians(latitude))
    dl = (2 / 15) * math.degrees(math.acos(st2 * st3))
    return round(dl, 2)
