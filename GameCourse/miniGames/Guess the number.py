import random
import os


def clear():
    os.system("cls")


def _input():
    while y == 0:
        b = input("Guess the number : ")
        clear()
        if b.isdigit() is True:
            b1 = int(b)
            return b1
        else:
            print("Enter only numbers")
	

def _loop(v1, a1, y1):
    while v1 != a1:
        y1 += 1
        if v1 < a1:
            print("The number you've entered is LOWER than the actual number so try again")
        elif v1 > a1:
            print("The number you've entered is HIGHER than the actual number so try again")
        v1 = _input()
        clear()
    y1 += 1
    print("Congrats you've entered the correct number in " + str(y1) + " tries")


y = 0
while y == 0:
    a = random.randint(1, 100)
    v = _input()
    clear()
    _loop(v, a, y)
