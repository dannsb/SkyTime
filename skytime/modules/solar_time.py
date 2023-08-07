import math
import ephem


class SolarTime:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def calculate(self):
        observer = ephem.Observer()
        observer.lat = str(self.latitude)
        observer.lon = str(self.longitude)

        sun = ephem.Sun()

        # Calculate the sunrise and sunset times for today
        sunrise = observer.next_rising(sun)
        sunset = observer.next_setting(sun)

        # Convert the results to local time
        sunrise_local = ephem.localtime(sunrise)
        sunset_local = ephem.localtime(sunset)

        self.sunRise = sunrise_local
        self.sunSet = sunset_local

    def getSunSet(self):
        return self.sunSet.strftime("%H:%M")

    def getSunRise(self):
        return self.sunRise.strftime("%H:%M")
