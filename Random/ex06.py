#Exercise 06:
import random 


listString  = input("enter a sentance:")
listString = str(listString)
a = ""
for n in range( len(listString),0,-1):
     a += listString[n-1]
if listString == a:
    print("list is plaindrom")
else:
    print("list is not plaindrom")

