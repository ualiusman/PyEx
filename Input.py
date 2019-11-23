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
year, month, day = map(int,dob.split("-"))
date = datetime.date(year,month,day)
date = addYear(date,100)
d = date.strftime("%Y-%m-%d")
print( name + " will turn 100 in " +d)