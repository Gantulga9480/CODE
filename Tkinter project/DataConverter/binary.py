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
        print(res)
        return u
    else:
        print("wrong input")

x = input("enter val: ")
binary_converter(x)