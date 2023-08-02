import json
from requests import get


def getLunarDay(timestamp):
    try:
        result = get("https://api.keybit.ir/time/", {"timestamp": timestamp}).json()
        return result["date"]["other"]["ghamari"]["usual"]["en"]

    except Exception as err:
        print(err)


def getMoonPhase(lunarDay):
    moonPhasesJson = open("./moonphases.json")
    moonPhases = json.load(moonPhasesJson)
    pass


def getMoonRise():
    pass


def getMoonSet():
    pass
