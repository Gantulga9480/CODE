import os


def clear():
    os.system('cls')


def octal():
    t = input("Enter number = ")
    r = int(t)
    print("                                      " + oct(r))


def binary():
    t = input("Enter number = ")
    r = int(t)
    print("                                      " + bin(r))


def hexadecimal():
    t = input("Enter number = ")
    r = int(t)
    print("                                      " + hex(r))


def decimal():
    t = input("Enter number = ")
    res = [int(q) for q in str(t)]
    u = 0
    r = len(res) - 1
    for i in range(0, len(res)):
        if res[i] == 1:
            u = u + pow(2, r)
        elif res[i] == 0:
            pass
        else:
            print("                                      " + "WRONG INPUT")
            break
        r -= 1
    space = "                                      {}"
    print(space.format(u))


while True:

    print("""2 ----- 1
    8 ----- 2
    10 ---- 3
    16 ---- 4
    CLEAR - 5""")

    x = int(input('Select = '))


