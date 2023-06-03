import json

moonPhasesJson = open("./moonphases.json")
moonPhases = json.load(moonPhasesJson)
lunarDay = float(input("Write the lunar day to show the approximate time of moonrise: "))
# 14 lunar day
# 13 sunny

# Starry Night
# June 3 : 7:25
# June 4 : 8:35
# June 5 : 9:41
# June 6 : 10:42
# June 7 : 11:31

# Delux Moon 
# June 3 : 17:56
# June 4 : 19:05
# June 5 : 20:12
# June 6 : 21:13
# June 7 : 22:05

# Moon Phase Calender
# June 3 : 18:24
# June 4 : 19:33
# June 5 : 20:40
# June 6 : 21:41
# June 7 : 22:34


# Phases of Moon
# June 3 : 6:25
# June 4 : 7.34
# June 5 : 8:41
# June 6 : 9:42
# June 7 : 10:34


try:
    time_dict = {0: "06:55", 1: "07:55", 3: "08:30", 4: "09:05", 5: "09:40", 6: "10:30", 7: "11:30", 8: "12:15", 9: "13:15", 10: "14:10", 11: "15:10", 12: "16:05", 13: "17:05", 14: "18:05", 15: "19:05", 16: "19:45", 17: "20:45", 18: "21:46", 19: "22:55", 20: "00:00", 21: "01:05", 22: "02:05", 23: "02:58", 24: "03:43", 25: "04:25", 26: "05:00", 27: "05:31", 28: "06:00", 29: "06:32"}
    newDict = {}
    
    if lunarDay in time_dict:
        print(time_dict[lunarDay])
    else:
        print("Error")
except ValueError:
    print("just enter number")