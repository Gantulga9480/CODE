import math as mt
import os

def clear():
    os.system("cls")


while True:
    a1 = input("x^2 = ")
    b1 = input("x^1 = ")
    c1 = input("x^0 = ")

    a = float(a1)
    b = float(b1)
    c = float(c1)

    print("\n\n")

    print(a1 + 'x^2' + "+" + b1 + "x" + "+" + c1 + "= 0", "\n\n")
    d = b ** 2 + (-4) * a * c

    if d < 0:
        print("Huurmag\n")
        x1_1 = (-1 * b ) / (2 * a)

        x1_2 = (mt.sqrt(-1 * d)) / (2 * a)

        x2_1 = (-1 * b ) / (2 * a)

        x2_2 = (-1 * mt.sqrt(-1 * d)) / (2 * a)

        print("x1: " + str(x1_1) + " + " + str(x1_2)  + "\n" + "x2: " + str(x2_1) + " + " + str(x2_2))
    else:
        x1 = (-1 * b + mt.sqrt(d)) / (2 * a)

        x2 = (-1 * b - mt.sqrt(d)) / (2 * a)

        if x1 == x2:
            print("x(1,2) = ", x1)
        else:
            print("x1 = ", x1, "\n""x2 = ", x2)

    print("\n\n")

    input("Press any key to continue!")

    clear()
