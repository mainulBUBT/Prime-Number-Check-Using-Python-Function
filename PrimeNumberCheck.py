import math

def checkPrimeNumber(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    root = math.sqrt(number)
    for i in range(3,int(root)):
        if number % i == 0:
            return False
        i = i+2
    return True

while True:
    number = int(input("Enter: "))
    if number == 0:
        print("Not Prime")
        break
    if (checkPrimeNumber(number) == True):
        print("Prime Number")
    else:
        print("Not Prime")