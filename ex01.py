#Exercise 01:

import datetime
from datetime import timedelta


def addYear(d,year):
    try:
        return d.replace(year = d.year + year)
    except ValueError:
        return d + (date(d.year + year,1,1) - date(d.year,1,1))

name = input("what is you name? ")
dob = input("What is your DOB? ")
date  = datetime.date(2000,1,1)
try:
    year, month, day = map(int,dob.split("-"))
    date = datetime.date(year,month,day)
    date = addYear(date,100)
    d = date.strftime("%Y-%m-%d")
    print( name + " will turn 100 in " +d)
    nTime = input("How many times you want to print this message? ")
    nTime = int(nTime)
    for n in range(nTime):
        print( name + " will turn 100 in " +d)
except:
    print("enter date in yyyy-mm-dd format")

