#Exercise 03:
try:
    numberList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    limit = input("Enter a number as limit:")
    limitList = []
    limit = int(limit)
    for n in numberList:
        if n < limit:
            limitList.append(n)
        
    for n in limitList:
            print(n)
except:
    print("Invalid number")

