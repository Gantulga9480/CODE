import os

def clear():
    os.system("cls")
while True:
    x = input("Word : ")
    x1 = x.split(' ')
    y1 = []
    for items in x1:
        y = list(items)
        i = 0
        u = []
        for item in y:
            z = ord(item)
            if z == 1094:
                u.append(chr(119))
            elif z == 1091:
                u.append(chr(101))
            elif z == 1078:
                u.append(chr(114))
            elif z == 1101:
                u.append(chr(116))
            elif z == 1085:
                u.append(chr(121))
            elif z == 1075:
                u.append(chr(117))
            elif z == 1096:
                u.append(chr(105))
            elif z == 1199:
                u.append(chr(111))
            elif z == 1079:
                u.append(chr(112))
            elif z == 1081:
                u.append(chr(97))
            elif z == 1099:
                u.append(chr(115))
            elif z == 1073:
                u.append(chr(100))
            elif z == 1257:
                u.append(chr(102))
            elif z == 1072:
                u.append(chr(103))
            elif z == 1093:
                u.append(chr(104))
            elif z == 1088:
                u.append(chr(106))
            elif z == 1086:
                u.append(chr(107))
            elif z == 1083:
                u.append(chr(108))
            elif z == 1103:
                u.append(chr(122))
            elif z == 1095:
                u.append(chr(120))
            elif z == 1105:
                u.append(chr(99))
            elif z == 1089:
                u.append(chr(118))
            elif z == 1084:
                u.append(chr(98))
            elif z == 1080:
                u.append(chr(110))
            elif z == 1090:
                u.append(chr(109))
            elif z < 1000:
                u.append(chr(z))
            i += 1
        u.append(chr(32))
        o = ''.join(u)
        y1.append(o)
    print(''.join(y1))
    input("Press to clear")
    clear()
