import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
f = open("../data/childDetails.json", "r")
children = json.load(f)
f.close()

longestname = ""
longestcountname = 0
shortestname = ""
shortestcountname = 100

for child in children:
    if len(child["name"]) > longestcountname:
        longestname = child["name"]
        longestcountname = len(child["name"])
    elif len(child["name"]) < shortestcountname:
        shortestname = child["name"]
        shortestcountname = len(child["name"])

print ("Longest =>", longestname,"Shortest =>", shortestname)
print("")

highest = ""
highestincome = 0
lowest = ""
lowestincome = 10000000000000
income = 0

for child in children:
    income = 0
    for incomes in child["guardians"]:
        income = incomes["salary"] + income
    if income > highestincome:
            highestincome = income
            highest = child["name"]
    elif income < lowestincome:
            lowestincome = income
            lowest = child["name"]

print ("Highest =>", highest,highestincome, "Lowest =>", lowest,lowestincome)
print("")

hinheritance = 0
higher = ""
linheritance = 10000000
lower = ""
income = 0
siblingamount = 1
for child in children:
     income = 0
     siblingamount = 1
     for sibling in child["siblings"]:
          siblingamount = siblingamount + 1
     for incomes in child["guardians"]:
          income = incomes["salary"] + income
     if income/siblingamount < linheritance:
          linheritance = income/siblingamount
          lower = child["name"]    
     if income/siblingamount > hinheritance:
          hinheritance = income/siblingamount
          higher = child["name"]

print("Highest =>", higher,hinheritance,"Lowest =>", lower,linheritance)
print("")