#Exercise 20:

def find(number, number_to_find):
    for n in number:
      if n == number_to_find:
        return True
    return False

if __name__ == "__main__":
    numbers =[1,2,5,6,98,27,1]
    print(find(numbers,1))
    print(find(numbers,20))