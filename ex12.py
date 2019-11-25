#Exercise 12:
def fistLastEliOfList(lst):
    return (lst[0],lst[len(lst)-1])

l = [1,2,34,13,14,5,6]
first, last = fistLastEliOfList(l)
print("first:" + str(first))
print("last:" + str(last))