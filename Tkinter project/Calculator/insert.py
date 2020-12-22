class Insert:

    def __init__(self, expression=None):
        self.expression = expression
        self.x = list(self.expression)

    def __del__(self):
        # print("Insert deleted <---")
        pass

    def zero(self):
        lst = self.x.copy()
        zero_inserted = 0
        for index, item in enumerate(self.x):
            if item == "(":
                if self.x[index + 1] == "-":
                    lst.insert(index + 1 + zero_inserted, "0")
                    zero_inserted += 1
                else:
                    pass
            else:
                pass
        lst = "".join(lst)
        return lst

    def cross(self):
        a = self.x.copy()
        count = 0
        mul_count = 0
        for index, item in enumerate(self.x):
            count = index + 1
            if count == len(self.x):
                pass
            else:
                last = item
                nxt = self.x[count]
                if nxt == "+" or nxt == "-" or nxt == "×" or nxt == "/" or nxt == "^" or nxt == ")" or nxt == "." or nxt == "!" or nxt == "%":
                    pass
                elif last == "+" or last == "-" or last == "×" or last == "/" or last == "^" or last == "(" or last == "." or last == "%":
                    pass
                elif nxt.isdigit() and not last.isdigit():
                    a.insert(count + mul_count, "×")
                    mul_count += 1
                elif last.isdigit() and not nxt.isdigit():
                    a.insert(count + mul_count, "×")
                    mul_count += 1
        a = "".join(a)
        return a


    def fact_bracket(self):
        a = self.x.copy()
        bracket_enter = 0
        closed = False
        enter = False
        count = 0
        # print(self.x)
        for index, item in enumerate(self.x):
            if item == "!":
                closed = False
                enter = False
                # print("! index ", index)
                i = index
                a.insert(i + 1 + count, ")")
                # print(self.x[i - 1])
                if a[i - 1 + count] == ")":
                    enter = True
                else:
                    pass
                while not closed:
                    i -= 1
                    # print(a[i + count])
                    if enter:
                        # print("entered")
                        if a[i + count] == ")":
                            bracket_enter += 1
                        elif a[i + count] == "(":
                            bracket_enter -= 1
                            if bracket_enter == 0:
                                if a[i + count - 1] == "+" or a[i + count - 1] == "-" or a[i + count - 1] == "/" or a[i + count - 1] == "×" or a[i + count - 1] == "^":
                                    closed = True
                                    a.insert(i + count, "(")
                                    count += 2
                                else:
                                    enter = False
                        else:
                            pass
                    elif a[i + count] == "+" or a[i + count] == "-" or a[i + count] == "/" or a[i + count] == "×" or a[i + count] == "^" or a[i + count] == "(":
                        a.insert(i + 1 + count, "(")
                        count += 2
                        closed = True
                        # print("closed")
                    else:
                        #print(a[i + count])
                        pass
                    # print(count)
            else:
                pass
        a = "".join(a)
        return a

    def pow_bracket(self):
        # self.x.reverse()
        a = self.x.copy()
        count = 0
        enter_count = 0
        close_count = 0
        for index, item in enumerate(self.x):
            if item == "^":
                idx =  index
                ini_enter_br = False
                ini_close_br = False
                enter_br = False
                close_br = False
                while not enter_br:
                    idx -= 1
                    if ini_enter_br:
                        if idx == 0:
                            a.insert(idx, "(")
                            count += 1
                            enter_count += 1
                            enter_br = True
                        elif a[idx + count] == "(":
                            ini_enter_br = False
                        else:
                            pass
                    else:
                        if idx == 0:
                            a.insert(idx, "(")
                            count += 1
                            enter_count += 1
                            enter_br = True
                        elif a[idx + count] == "(" and enter_count == 0:
                            enter_br = True
                        elif a[idx + count] == "(":
                            enter_count -= 1
                        elif a[idx + count] == ")" and close_count == 0:
                            ini_enter_br = True
                        elif a[idx + count] == ")":
                            close_count -= 1
                        elif a[idx + count] == "+" or a[idx + count] == "-":
                            a.insert(idx + count + 1, "(")
                            count += 1
                            enter_count += 1
                            enter_br = True
                        else:
                            pass
                idx = index
                while not close_br:
                    idx += 1
                    if ini_close_br:
                        if a[idx + count] == ")":
                            ini_close_br = False
                        else:
                            pass
                    else:
                        if idx + count == len(a):
                            a.insert(len(a), ")")
                            close_br = True
                        if a[idx + count] == ")":
                            close_br = True
                        elif a[idx + count] == "(" and close_count == 0:
                            ini_close_br = True
                        elif a[idx + count] == "+" or a[idx + count] == "-" or a[idx + count] == "×" or a[idx + count] == "/" or a[idx + count] == "^":
                            a.insert(idx + count, ")")
                            count += 1
                            close_count += 1
                            close_br = True
                        else:
                            pass
            elif item == "+" or item == "-" or item == "/" or item == "×":
                enter_count = 0
            else:
                pass
        a = "".join(a)
        return a

    def bracket(self):
        a = self.x.copy()
        count = 0
        enter_count = 0
        close_count = 0
        for index, item in enumerate(self.x):
            if item == "×" or item == "/":
                idx =  index
                ini_enter_br = False
                ini_close_br = False
                enter_br = False
                close_br = False
                while not enter_br:
                    idx -= 1
                    if ini_enter_br:
                        if idx == 0:
                            a.insert(idx, "(")
                            count += 1
                            enter_count += 1
                            enter_br = True
                        elif a[idx + count] == "(":
                            ini_enter_br = False
                        else:
                            pass
                    else:
                        if idx == 0:
                            a.insert(idx, "(")
                            count += 1
                            enter_count += 1
                            enter_br = True
                        elif a[idx + count] == "(" and enter_count == 0:
                            a.insert(idx + count, "(")
                            enter_br = True
                        elif a[idx + count] == "(":
                            enter_count -= 1
                        elif a[idx + count] == ")" and close_count == 0:
                            ini_enter_br = True
                            # print("here")
                        elif a[idx + count] == ")":
                            close_count -= 1
                        elif a[idx + count] == "+" or a[idx + count] == "-" or a[idx + count] == "(":
                            a.insert(idx + count + 1, "(")
                            count += 1
                            enter_count += 1
                            enter_br = True
                        else:
                            pass
                idx = index
                while not close_br:
                    idx += 1
                    if ini_close_br:
                        if a[idx + count] == ")":
                            ini_close_br = False
                        else:
                            pass
                    else:
                        if idx + count == len(a):
                            a.insert(len(a), ")")
                            close_br = True
                        if a[idx + count] == ")":
                            close_br = True
                        elif a[idx + count] == "(" and close_count == 0:
                            ini_close_br = True
                        elif a[idx + count] == "+" or a[idx + count] == "-" or a[idx + count] == "×" or a[idx + count] == "/" or a[idx + count] == "^":
                            a.insert(idx + count, ")")
                            count += 1
                            close_count += 1
                            close_br = True
                        else:
                            pass
            elif item == "+" or item == "-":
                enter_count = 0
        if a[0] == "(" and a[len(a)-1] == ")":
            bracket = 0
            sign = 0
            for i in a:
                if i == "(":
                    bracket += 1
                elif i == "+" or i == "-" or i == "/" or i == "×" or i == "^":
                    sign += 1
            if sign > bracket:
                a.insert(0,"(")
                a.insert(len(a), ")")
            else:
                pass
        else:
            a.insert(0,"(")
            a.insert(len(a), ")")
        a = "".join(a)
        return a