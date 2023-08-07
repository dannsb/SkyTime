from modules.lunar_time import LunarTime
from modules.solar_time import SolarTime
from time import sleep
from persiantools.jdatetime import JalaliDate
from date_helper import getDayOfYear, jalaliToGregorian, gregorianToLunarDay
from banner.banner import printBanner


class main:
    def __init__(self):
        pass

    def getUserDate(self):
        today = JalaliDate.today().strftime("%Y/%m/%d")
        userDate = input(f"\nPlease enter your date [{today}] : ")
        if not userDate:
            userDate = today
        return userDate

    def run(self):
        try:
            printBanner()
            userDate = self.getUserDate()
            year, month, day = map(int, userDate.split("/"))
            gregorianDate = jalaliToGregorian(year, month, day)
            lunarDate = gregorianToLunarDay(
                gregorianDate.year, gregorianDate.month, gregorianDate.day
            )

            dayOfYear = getDayOfYear(month, day)
            solar = SolarTime(29.5916, 52.5839)  # latiude and longitude of shiraz
            solar.calculate()
            sunRiseTime = solar.getSunRise()
            sunSetTime = solar.getSunSet()
            lunar = LunarTime(lunarDate)
            moonPhase = lunar.getMoonPhase()

            print(
                f"""
            date : {userDate}
            lunarDate : {lunarDate}
            sun rise : {sunRiseTime}
            sun set : {sunSetTime}
            """
            )

        except KeyboardInterrupt:
            exit()

        except Exception as err:
            print(err)


if __name__ == "__main__":
    main().run()
