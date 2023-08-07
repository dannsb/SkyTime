import json
import ephem


class LunarTime:
    def __init__(self, lunarDate):
        self.lunarDate = lunarDate
        pass

    def calculate(self):
        pass

    def getMoonPhase(self):
        lunarDay = self.lunarDate.split("/")[-1]
        moonPhasesJson = open("./modules/moonphases.json")
        moonPhases = json.load(moonPhasesJson)
        pass

    def getMoonRise(self):
        return self.moonRise.strftime("%H:%M")

    def getMoonSet(self):
        return self.moonSet.strftime("%H:%M")
