#Exercise 02:


num = input("Enter a number:")
check = input("Enter a check:")
try:
    check = int(check)
    num  = int(num)
    result = num % 2
    checkResult = num / 2
    checkResult = checkResult % 2
    if result == 0:
        print("number is even")
    else:
        print("number is odd")

    if num % 4 ==0:
        print("number is multiple of 4 as well")

    if checkResult == 0:
        print("check is evenly multiple to number")
except:
    print("Number is invalid")