import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
f = open("../data/1000-largest-us-cities.json", "r")
cities = json.load(f)
f.close()

cities1 = ""
for city in cities:
    if city["state"] == "Kansas":
        cities1 = cities1 + city["city"] + " "

print("The Kansas cities that are in this list include:", cities1)

longest = ""
longestcount = 0
for city in cities:
    if len(city["city"]) > longestcount:
        longest = city["city"]
        longestcount = len(city["city"])
    else:
        pass

print("The longest city name is ", longest, "with ",longestcount, "letters.")

north = ""
northcount = -10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
south = ""
southcount = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
west = ""
westcount = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
east = ""
eastcount = -10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

for city in cities:
    if city["latitude"] > northcount:
        northcount = city["latitude"]
        north = city["city"]
    elif city["latitude"] < southcount:
        southcount = city["latitude"]
        south = city["city"]
    if city["longitude"] < westcount:
        westcount = city["longitude"]
        west = city["city"]
    elif city["longitude"] > eastcount:
        eastcount = city["longitude"]
        east = city["city"]
    else:
        pass

print(north,south,west,east)

grow = ""
growing = 0
shrink = ""
shrinking = 100

for city in cities:
    rate = city["growth_from_2000_to_2013"].split("%")
    rate = rate[0]
    if rate != "":
        rate = int(float(rate))
        if rate > growing:
            growing = rate
            grow = city["city"]
        if rate < shrinking:
            shrinking = rate
            shrink = city["city"]

print(grow,growing,shrink,shrinking)