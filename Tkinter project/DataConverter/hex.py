hex_val = {
    "0": "0000",
    "1": "0001",
    "2": "0011",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

def hex_converter(val):
    res = list()
    is_valid = True
    t = val
    lst = [int(q) for q in str(t)]
    u = 0
    r = len(lst) - 1
    for i in range(0, len(lst)):
        if lst[i] == 1:
            u = u + pow(2, r)
        elif lst[i] == 0:
            pass
        else:
            is_valid = False
            break
        r -= 1
    if is_valid:
        res.append(u)
        res.append(bin(u))
        res.append(oct(u))
        print(res)
        return u
    else:
        print("wrong input")

x = input("enter val: ")

x = list(x)
new = list()
for item in x:
    new.append(hex_val.get(item, "2"))

new = "".join(new)
hex_converter(new)