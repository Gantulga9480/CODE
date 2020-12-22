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

octal_val = {
    "0": "000",
    "1": "001",
    "2": "010",
    "3": '011',
    "4": "100",
    "5": "101",
    "6": "110",
    "7": "111",
}

def hex_converter(val):
    x = list(val)
    new = list()
    for item in x:
        new.append(hex_val.get(item, "2"))
    new = "".join(new)
    res = list()
    is_valid = True
    lst = [int(q) for q in str(new)]
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
        res.append(hex(u))
        return res
    else:
        return False

def octal_converter(val):
    x = list(val)
    new = list()
    for item in x:
        new.append(hex_val.get(item, "2"))
    new = "".join(new)
    res = list()
    is_valid = True
    lst = [int(q) for q in str(new)]
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
        res.append(hex(u))
        return res.copy()
    else:
        return False

def binary_converter(val):
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
        res.append(hex(u))
        return res.copy()
    else:
        return False

def decimal_converter(val):
    res = list()
    res.append(val)
    res.append(bin(val))
    res.append(oct(val))
    res.append(hex(val))
    return res.copy()