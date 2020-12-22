def pow_bracket(self):
        a = self.x.copy()
        count = 0
        enter_count = 0
        close_count = 0
        for index, item in enumerate(self.x):
            if item == "^":
                idx = index
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
                        elif a[idx + count] == "+" or a[idx + count] == "-" or a[idx + count] == "×" or a[idx + count] == "/":
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
                            a.insert(idx + count, ")")
                            count += 1
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