import math as mt
# ---------------------------------------------------------------------------
class ArithmeticUnit:

    def __init__(self, rad=True, inv=False, mode=None):
        self.rad = rad
        self.inv = inv
        self.mode = mode
        self.result = 0

    def singleInput(self, flag=None, value=None, index=None):
        val = 0
        if self.mode[index] == "default":
            if flag:
                if value == "e":
                    self.result = mt.e
                elif value == "π":
                    self.result = mt.pi
            else:
                self.result = float(value)
        elif self.mode[index] == "sin":
            if not self.inv:
                if flag:
                    if value == "e":
                        if self.rad:
                            self.result = mt.sin(mt.e)
                        else:
                            self.result = mt.sin(mt.e/180*mt.pi)
                    elif value == "π":
                        if self.rad:
                            self.result = mt.sin(mt.pi)
                        else:
                            self.result = mt.sin(mt.pi/180*mt.pi)
                else:
                    val = float(value)
                    if self.rad:
                        self.result = mt.sin(val)
                    else:
                        self.result = mt.sin(val/180*mt.pi)
            elif self.inv:
                if flag:
                    raise ValueError
                else:
                    val = float(value)
                    if -1 <= val <= 1:
                        if self.rad:
                            self.result = mt.asin(val)
                        elif not self.rad:
                            self.result = mt.asin(val)/mt.pi*180
                    else:
                        raise ValueError
        elif self.mode[index] == "cos":
            if not self.inv:
                if flag:
                    if value == "e":
                        if self.rad:
                            self.result = mt.cos(mt.e)
                        else:
                            self.result = mt.cos(mt.e/180*mt.pi)
                    elif value == "π":
                        if self.rad:
                            self.result = mt.cos(mt.pi)
                        else:
                            self.result = mt.cos(mt.pi/180*mt.pi)
                else:
                    val = float(value)
                    if self.rad:
                        self.result = mt.cos(val)
                    elif not self.rad:
                        self.result = mt.cos(mt.pi * val / 180)
            elif self.inv:
                if flag:
                    raise ValueError
                else:
                    val = float(value)
                    if -1 <= val <= 1:
                        if self.rad:
                            self.result = mt.acos(val)
                        elif not self.rad:
                            self.result = mt.acos(val)/mt.pi*180
                    else:
                        raise ValueError
        elif self.mode[index] == "tan":
            if not self.inv:
                if flag:
                    if value == "e":
                        if self.rad:
                            self.result = mt.tan(mt.e)
                        else:
                            self.result = mt.tan(mt.e/180*mt.pi)
                    elif value == "π":
                        if self.rad:
                            self.result = mt.tan(mt.pi)
                        else:
                            self.result = mt.tan(mt.pi/180*mt.pi)
                else:
                    val = float(value)
                    if self.rad:
                        self.result = mt.tan(val)
                    else:
                        self.result = mt.tan(val/180*mt.pi)
            elif self.inv:
                if flag:
                    if value == "e":
                        if self.rad:
                            self.result = mt.atan(mt.e)
                        else:
                            self.result = mt.atan(mt.e)/mt.pi*180
                    elif value == "π":
                        if self.rad:
                            self.result = mt.atan(mt.pi)
                        else:
                            self.result = mt.atan(mt.pi)/mt.pi*180
                else:
                    val = float(value)
                    if self.rad:
                        self.result = mt.atan(val)
                    elif not self.rad:
                        self.result = mt.atan(val)/mt.pi*180
        elif self.mode[index] == "ln":
            if flag:
                if value == "e":
                    self.result = mt.log(mt.e)
                elif value == "π":
                    self.result = mt.log(mt.pi)
            else:
                val = float(value)
                if val >= 0:
                    self.result = mt.log(val)
                else:
                    print("Value Error")
                    raise ValueError
        elif self.mode[index] == "log":
            if flag:
                if value == "e":
                    self.result = mt.log10(mt.e)
                elif value == "π":
                    self.result = mt.log10(mt.pi)
            else:
                val = float(value)
                if val >= 0:
                    self.result = mt.log10(val)
                else:
                    raise ValueError
        elif self.mode[index] == "sqrt":
            if flag:
                if value == "e":
                    self.result = mt.sqrt(mt.e)
                elif value == "π":
                    self.result = mt.sqrt(mt.pi)
            else:
                val = float(value)
                if val >= 0:
                    self.result = mt.sqrt(val)
                else:
                    raise ValueError
        elif self.mode[index] == "!":
            if flag:
                raise ValueError
            else:
                val = float(value)
                if val - int(value) == 0.0:
                    self.result = mt.factorial(val)
                else:
                    raise ValueError
        print("result in calculate", self.result)
        return self.result

    def fact_calculate(self, flag, value):
        if flag:
            raise ValueError
        else:
            val = float(value)
            if val - int(val) < 0.00000000001:
                self.result = mt.factorial(int(val))
            else:
                raise ValueError
        return self.result

    def doubleInput(self, flag=None, first=None, second=None, index=None, sign=None):
        if self.mode[index] == "default":
            if not flag[0] and not flag[1]:
                if sign == "+":
                    self.result = float(first) + float(second)
                elif sign == "-":
                    self.result = float(first) - float(second)
                elif sign == "/":
                    if float(second) == 0.0:
                        raise ZeroDivisionError
                    else:
                        self.result = float(first) / float(second)
                elif sign == "×":
                    self.result = float(first) * float(second)
                elif sign == "^":
                    self.result = float(first) ** float(second)
                elif sign == "%":
                    self.result = (float(first) / 100) * float(second)
            elif flag[0] and not flag[1]:
                if first == "π":
                    first = mt.pi
                elif first == "e":
                    first = mt.e
                if sign == "+":
                    self.result = first + float(second)
                elif sign == "-":
                    self.result = first - float(second)
                elif sign == "/":
                    if float(second) == 0.0:
                        raise ZeroDivisionError
                    else:
                        self.result = first / float(second)
                elif sign == "×":
                    self.result = first * float(second)
                elif sign == "^":
                    self.result = first ** float(second)
                elif sign == "%":
                    self.result = (first / 100) * float(second)
            elif not flag[0] and flag[1]:
                if second == "π":
                    second = mt.pi
                elif second == "e":
                    second = mt.e
                if sign == "+":
                    self.result = float(first) + second
                elif sign == "-":
                    self.result = float(first) - second
                elif sign == "/":
                    self.result = float(first) / second
                elif sign == "×":
                    self.result = float(first) * second
                elif sign == "^":
                    self.result = float(first) ** second
                elif sign == "%":
                    self.result = (float(first) / 100) * second
            elif flag[0] and flag[1]:
                if first == "π":
                    first = mt.pi
                elif first == "e":
                    first = mt.e
                if second == "π":
                    second = mt.pi
                elif second == "e":
                    second = mt.e
                if sign == "+":
                    self.result = first + second
                elif sign == "-":
                    self.result = first - second
                elif sign == "/":
                    self.result = first / second
                elif sign == "×":
                    self.result = first * second
                elif sign == "^":
                    self.result = first ** second
                elif sign == "%":
                    self.result = (first / 100) * second
# ------------------------------------- SIN -----------------------------------
        elif self.mode[index] == "sin":
            if not self.inv:
                if self.rad:
                    if not flag[0] and not flag[1]:
                        if sign == "+":
                            self.result = mt.sin(float(first) + float(second))
                        elif sign == "-":
                            self.result = mt.sin(float(first) - float(second))
                        elif sign == "/":
                            if float(second) == 0.0:
                                raise ZeroDivisionError
                            else:
                                self.result = mt.sin(float(first) / float(second))
                        elif sign == "×":
                            self.result = mt.sin(float(first) * float(second))
                        elif sign == "^":
                            self.result = mt.sin(float(first) ** float(second))
                        elif sign == "%":
                            self.result = mt.sin(float(first) / 100 * float(second))
                    elif flag[0] and not flag[1]:
                        if first == "π":
                            first = mt.pi
                        elif first == "e":
                            first = mt.e
                        if sign == "+":
                            self.result = mt.sin(first + float(second))
                        elif sign == "-":
                            self.result = mt.sin(first - float(second))
                        elif sign == "/":
                            if float(second) == 0.0:
                                raise ZeroDivisionError
                            else:
                                self.result = mt.sin(first / float(second))
                        elif sign == "×":
                            self.result = mt.sin(first * float(second))
                        elif sign == "^":
                            self.result = mt.sin(first ** float(second))
                        elif sign == "%":
                            self.result = mt.sin(first / 100 * float(second))
                    elif not flag[0] and flag[1]:
                        if second == "π":
                            second = mt.pi
                        elif second == "e":
                            second = mt.e
                        if sign == "+":
                            self.result = mt.sin(float(first) + second)
                        elif sign == "-":
                            self.result = mt.sin(float(first) - second)
                        elif sign == "/":
                            self.result = mt.sin(float(first) / second)
                        elif sign == "×":
                            self.result = mt.sin(float(first) * second)
                        elif sign == "^":
                            self.result = mt.sin(float(first) ** second)
                        elif sign == "%":
                            self.result = mt.sin(float(first) / 100 * second)
                    elif flag[0] and flag[1]:
                        if first == "π":
                            first = mt.pi
                        elif first == "e":
                            first = mt.e
                        if second == "π":
                            second = mt.pi
                        elif second == "e":
                            second = mt.e
                        if sign == "+":
                            self.result = mt.sin(first + second)
                        elif sign == "-":
                            self.result = mt.sin(first - second)
                        elif sign == "/":
                            self.result = mt.sin(first / second)
                        elif sign == "×":
                            self.result = mt.sin(first * second)
                        elif sign == "^":
                            self.result = mt.sin(first ** second)
                        elif sign == "%":
                            self.result = mt.sin(first / 100 * second)
                elif not self.rad:
                    if not flag[0] and not flag[1]:
                        first = float(first) / 180 * mt.pi
                        second = float(second) / 180 * mt.pi
                        if sign == "+":
                            self.result = mt.sin(first + second)
                        elif sign == "-":
                            self.result = mt.sin(first - second)
                        elif sign == "/":
                            if float(second) == 0.0:
                                raise ZeroDivisionError
                            else:
                                self.result = mt.sin(first / second)
                        elif sign == "×":
                            self.result = mt.sin(first * second)
                        elif sign == "^":
                            self.result = mt.sin(first ** second)
                        elif sign == "%":
                            self.result = mt.sin(first / 100 * second)
                    elif flag[0] and not flag[1]:
                        if first == "π":
                            first = mt.pi
                        elif first == "e":
                            first = mt.e
                        second = float(second) / 180 * mt.pi
                        if sign == "+":
                            self.result = mt.sin(first + second)
                        elif sign == "-":
                            self.result = mt.sin(first - second)
                        elif sign == "/":
                            if second == 0.0:
                                raise ZeroDivisionError
                            else:
                                self.result = mt.sin(first / second)
                        elif sign == "×":
                            self.result = mt.sin(first * second)
                        elif sign == "^":
                            self.result = mt.sin(first ** second)
                        elif sign == "%":
                            self.result = mt.sin(first / 100 * second)
                    elif not flag[0] and flag[1]:
                        if second == "π":
                            second = mt.pi
                        elif second == "e":
                            second = mt.e
                        first = float(first) / 180 * mt.pi
                        if sign == "+":
                            self.result = mt.sin(first + second)
                        elif sign == "-":
                            self.result = mt.sin(first - second)
                        elif sign == "/":
                            self.result = mt.sin(first / second)
                        elif sign == "×":
                            self.result = mt.sin(first * second)
                        elif sign == "^":
                            self.result = mt.sin(first ** second)
                        elif sign == "%":
                            self.result = mt.sin(first / 100 * second)
                    elif flag[0] and flag[1]:
                        if first == "π":
                            first = mt.pi
                        elif first == "e":
                            first = mt.e
                        if second == "π":
                            second = mt.pi
                        elif second == "e":
                            second = mt.e
                        if sign == "+":
                            self.result = mt.sin(first + second)
                        elif sign == "-":
                            self.result = mt.sin(first - second)
                        elif sign == "/":
                            self.result = mt.sin(first / second)
                        elif sign == "×":
                            self.result = mt.sin(first * second)
                        elif sign == "^":
                            self.result = mt.sin(first ** second)
                        elif sign == "%":
                            self.result = mt.sin(first / 100 * second)
            elif self.inv:
                if self.rad:
                    if flag[0] or flag[1]:
                        raise ValueError
                    elif not flag[0] and not flag[1]:
                        if sign == "+":
                            if -1 <= float(first) + float(second) <= 1:
                                self.result = mt.asin(float(first) + float(second))
                            else:
                                raise ValueError
                        elif sign == "-":
                            if -1 <= float(first) - float(second) <= 1:
                                self.result = mt.asin(float(first) - float(second))
                            else:
                                raise ValueError
                        elif sign == "/":
                            if -1 <= float(first) / float(second) <= 1:
                                self.result = mt.asin(float(first) / float(second))
                            else:
                                raise ValueError
                        elif sign == "×":
                            if -1 <= float(first) * float(second) <= 1:
                                self.result = mt.asin(float(first) * float(second))
                            else:
                                raise ValueError
                        elif sign == "^":
                            if -1 <= float(first) ** float(second) <= 1:
                                self.result = mt.asin(float(first) ** float(second))
                            else:
                                raise ValueError
                        elif sign == "%":
                            if -1 <= float(first) / 100 * float(second) <= 1:
                                self.result = mt.asin(float(first) / 100 * float(second))
                            else:
                                raise ValueError
                    else:
                        raise ValueError
                if not self.rad:
                    if flag[0] or flag[1]:
                        raise ValueError
                    elif not flag[0] and not flag[1]:
                        if sign == "+":
                            if -1 <= float(first) + float(second) <= 1:
                                self.result = mt.asin(float(first) + float(second))
                                self.result = self.result / mt.pi * 180
                            else:
                                raise ValueError
                        elif sign == "-":
                            if -1 <= float(first) - float(second) <= 1:
                                self.result = mt.asin(float(first) - float(second))
                                self.result = self.result / mt.pi * 180
                            else:
                                raise ValueError
                        elif sign == "/":
                            if -1 <= float(first) / float(second) <= 1:
                                self.result = mt.asin(float(first) / float(second))
                                self.result = self.result / mt.pi * 180
                            else:
                                raise ValueError
                        elif sign == "×":
                            if -1 <= float(first) * float(second) <= 1:
                                self.result = mt.asin(float(first) * float(second))
                                self.result = self.result / mt.pi * 180
                            else:
                                raise ValueError
                        elif sign == "^":
                            if -1 <= float(first) ** float(second) <= 1:
                                self.result = mt.asin(float(first) ** float(second))
                                self.result = self.result / mt.pi * 180
                            else:
                                raise ValueError
                        elif sign == "%":
                            if -1 <= float(first) / 100 * float(second) <= 1:
                                self.result = mt.asin(float(first) / 100 * float(second))
                                self.result = self.result / mt.pi * 180
                            else:
                                raise ValueError
                    else:
                        raise ValueError
# ------------------------------------- COS -----------------------------------
        elif self.mode[index] == "cos":
            if not self.inv:
                if self.rad:
                    if not flag[0] and not flag[1]:
                        if sign == "+":
                            self.result = mt.cos(float(first) + float(second))
                        elif sign == "-":
                            self.result = mt.cos(float(first) - float(second))
                        elif sign == "/":
                            if float(second) == 0.0:
                                raise ZeroDivisionError
                            else:
                                self.result = mt.cos(float(first) / float(second))
                        elif sign == "×":
                            self.result = mt.cos(float(first) * float(second))
                        elif sign == "^":
                            self.result = mt.cos(float(first) ** float(second))
                        elif sign == "%":
                            self.result = mt.cos(float(first) / 100 * float(second))
                    elif flag[0] and not flag[1]:
                        if first == "π":
                            first = mt.pi
                        elif first == "e":
                            first = mt.e
                        if sign == "+":
                            self.result = mt.cos(first + float(second))
                        elif sign == "-":
                            self.result = mt.cos(first - float(second))
                        elif sign == "/":
                            if float(second) == 0.0:
                                raise ZeroDivisionError
                            else:
                                self.result = mt.cos(first / float(second))
                        elif sign == "×":
                            self.result = mt.cos(first * float(second))
                        elif sign == "^":
                            self.result = mt.cos(first ** float(second))
                        elif sign == "%":
                            self.result = mt.cos(first / 100 * float(second))
                    elif not flag[0] and flag[1]:
                        if second == "π":
                            second = mt.pi
                        elif second == "e":
                            second = mt.e
                        if sign == "+":
                            self.result = mt.cos(float(first) + second)
                        elif sign == "-":
                            self.result = mt.cos(float(first) - second)
                        elif sign == "/":
                            self.result = mt.cos(float(first) / second)
                        elif sign == "×":
                            self.result = mt.cos(float(first) * second)
                        elif sign == "^":
                            self.result = mt.cos(float(first) ** second)
                        elif sign == "%":
                            self.result = mt.cos(float(first) / 100 * second)
                    elif flag[0] and flag[1]:
                        if first == "π":
                            first = mt.pi
                        elif first == "e":
                            first = mt.e
                        if second == "π":
                            second = mt.pi
                        elif second == "e":
                            second = mt.e
                        if sign == "+":
                            self.result = mt.cos(first + second)
                        elif sign == "-":
                            self.result = mt.cos(first - second)
                        elif sign == "/":
                            self.result = mt.cos(first / second)
                        elif sign == "×":
                            self.result = mt.cos(first * second)
                        elif sign == "^":
                            self.result = mt.cos(first ** second)
                        elif sign == "%":
                            self.result = mt.cos(first / 100 * second)
                elif not self.rad:
                    if not flag[0] and not flag[1]:
                        if sign == "+":
                            first = float(first) / 180 * mt.pi
                            second = float(second) / 180 * mt.pi
                            self.result = mt.cos(first + second)
                        elif sign == "-":
                            first = float(first) / 180 * mt.pi
                            second = float(second) / 180 * mt.pi
                            self.result = mt.cos(first - second)
                        elif sign == "/":
                            if float(second) == 0.0:
                                raise ZeroDivisionError
                            else:
                                first = (float(first) / float(second)) / 180 * mt.pi
                                self.result = mt.cos(first)
                        elif sign == "×":
                            first = (float(first) * float(second)) / 180 * mt.pi
                            self.result = mt.cos(first)
                        elif sign == "^":
                            first = (float(first) ** float(second)) / 180 * mt.pi
                            self.result = mt.cos(first)
                        elif sign == "%":
                            first = (float(first) / 100 * float(second)) / 180 * mt.pi
                            self.result = mt.cos(first)
                    elif flag[0] and not flag[1]:
                        if first == "π":
                            first = 180
                        elif first == "e":
                            first = mt.e
                        if sign == "+":
                            second = float(second) / 180 * mt.pi
                            self.result = mt.cos(first + second)
                        elif sign == "-":
                            second = float(second) / 180 * mt.pi
                            self.result = mt.cos(first - second)
                        elif sign == "/":
                            if second == 0.0:
                                raise ZeroDivisionError
                            else:
                                first = (first / float(second)) / 180 * mt.pi 
                                self.result = mt.cos(first)
                        elif sign == "×":
                            first = (first * float(second)) / 180 * mt.pi 
                            self.result = mt.cos(first * second)
                        elif sign == "^":
                            first = (first ** float(second)) / 180 * mt.pi 
                            self.result = mt.cos(first ** second)
                        elif sign == "%":
                            first = (first / 100 * float(second)) / 180 * mt.pi 
                            self.result = mt.cos(first / 100 * second)
                    elif not flag[0] and flag[1]:
                        if second == "π":
                            second = 180
                        elif second == "e":
                            second = mt.e
                        if sign == "+":
                            first = float(first) / 180 * mt.pi
                            self.result = mt.cos(first + second)
                        elif sign == "-":
                            first = float(first) / 180 * mt.pi
                            self.result = mt.cos(first - second)
                        elif sign == "/":
                            first = (float(first) / second) / 180 * mt.pi
                            self.result = mt.cos(first / second)
                        elif sign == "×":
                            first = (float(first) * second) / 180 * mt.pi
                            self.result = mt.cos(first * second)
                        elif sign == "^":
                            first = (float(first) ** second) / 180 * mt.pi
                            self.result = mt.cos(first ** second)
                        elif sign == "%":
                            first = (float(first) / 100 * second) / 180 * mt.pi
                            self.result = mt.cos(first / 100 * second)
                    elif flag[0] and flag[1]:
                        if first == "π":
                            first = 180
                        elif first == "e":
                            first = mt.e
                        if second == "π":
                            second = 180
                        elif second == "e":
                            second = mt.e
                        if sign == "+":
                            self.result = mt.cos(first + second)
                        elif sign == "-":
                            self.result = mt.cos(first - second)
                        elif sign == "/":
                            first = (first / second) / 180 * mt.pi
                            self.result = mt.cos(first)
                        elif sign == "×":
                            first = (first * second) / 180 * mt.pi
                            self.result = mt.cos(first)
                        elif sign == "^":
                            first = (first ^ second) / 180 * mt.pi
                            self.result = mt.cos(first ** second)
                        elif sign == "%":
                            first = (first / 100 * second) / 180 * mt.pi
                            self.result = mt.cos(first / 100 * second)
            elif self.inv:
                if self.rad:
                    if flag[0] or flag[1]:
                        raise ValueError
                    elif not flag[0] and not flag[1]:
                        if sign == "+":
                            if -1 <= float(first) + float(second) <= 1:
                                self.result = mt.asin(float(first) + float(second))
                            else:
                                raise ValueError
                        elif sign == "-":
                            if -1 <= float(first) - float(second) <= 1:
                                self.result = mt.asin(float(first) - float(second))
                            else:
                                raise ValueError
                        elif sign == "/":
                            if float(second) != 0.0:
                                if -1 <= float(first) / float(second) <= 1:
                                    self.result = mt.asin(float(first) / float(second))
                                else:
                                    raise ValueError
                            else:
                                raise ValueError
                        elif sign == "×":
                            if -1 <= float(first) * float(second) <= 1:
                                self.result = mt.asin(float(first) * float(second))
                            else:
                                raise ValueError
                        elif sign == "^":
                            if -1 <= float(first) ** float(second) <= 1:
                                self.result = mt.asin(float(first) ** float(second))
                            else:
                                raise ValueError
                        elif sign == "%":
                            if -1 <= float(first) / 100 * float(second) <= 1:
                                self.result = mt.asin(float(first) / 100 * float(second))
                            else:
                                raise ValueError
                    else:
                        raise ValueError
                if not self.rad:
                    if flag[0] or flag[1]:
                        raise ValueError
                    elif not flag[0] and not flag[1]:
                        if sign == "+":
                            if -1 <= float(first) + float(second) <= 1:
                                self.result = mt.asin(float(first) + float(second))
                                self.result = self.result / mt.pi * 180
                            else:
                                raise ValueError
                        elif sign == "-":
                            if -1 <= float(first) - float(second) <= 1:
                                self.result = mt.asin(float(first) - float(second))
                                self.result = self.result / mt.pi * 180
                            else:
                                raise ValueError
                        elif sign == "/":
                            if float(second) != 0.0:
                                if -1 <= float(first) / float(second) <= 1:
                                    self.result = mt.asin(float(first) / float(second))
                                    self.result = self.result / mt.pi * 180
                                else:
                                    raise ValueError
                            else:
                                raise ValueError
                        elif sign == "×":
                            if -1 <= float(first) * float(second) <= 1:
                                self.result = mt.asin(float(first) * float(second))
                                self.result = self.result / mt.pi * 180
                            else:
                                raise ValueError
                        elif sign == "^":
                            if -1 <= float(first) ** float(second) <= 1:
                                self.result = mt.asin(float(first) ** float(second))
                                self.result = self.result / mt.pi * 180
                            else:
                                raise ValueError
                        elif sign == "%":
                            if -1 <= float(first) / 100 * float(second) <= 1:
                                self.result = mt.asin(float(first) / 100 * float(second))
                                self.result = self.result / mt.pi * 180
                            else:
                                raise ValueError
                    else:
                        raise ValueError

# --------------------------------------- sqrt ---------------------------------------------
        elif self.mode[index] == "sqrt":
            if first == "π":
                first = mt.pi
            elif first == "e":
                first = mt.e
            else:
                first = float(first)

            if second == "π":
                second = mt.pi
            elif second == "e":
                second = mt.e
            else:
                second = float(second)

            if sign == "+":
                if first + second >= 0:
                    self.result = mt.sqrt(first + second)
                else:
                    raise ValueError
            elif sign == "-":
                if first - second >= 0:
                    self.result = mt.sqrt(first - second)
                else:
                    raise ValueError
            elif sign == "×":
                if first * second >= 0:
                    self.result = mt.sqrt(first * second)
                else:
                    raise ValueError
            elif sign == "/":
                if first / second >= 0:
                    self.result = mt.sqrt(first / second)
                else:
                    raise ValueError
            elif sign == "^":
                if first ** second >= 0:
                    self.result = mt.sqrt(first ** second)
                else:
                    raise ValueError
            elif sign == "%":
                if first / 100 * second >= 0:
                    self.result = mt.sqrt(first / 100 * second)
                else:
                    raise ValueError

# ---------------------------------- ln ---------------------------------------
        elif self.mode[index] == "ln":
            if first == "π":
                first = mt.pi
            elif first == "e":
                first = mt.e
            else:
                first = float(first)

            if second == "π":
                second = mt.pi
            elif second == "e":
                second = mt.e
            else:
                second = float(second)

            if sign == "+":
                if first + second >= 0:
                    self.result = mt.log(first + second)
                else:
                    raise ValueError
            elif sign == "-":
                if first - second >= 0:
                    self.result = mt.log(first - second)
                else:
                    raise ValueError
            elif sign == "/":
                if first / second >= 0:
                    self.result = mt.log(first / second)
                else:
                    raise ValueError
            elif sign == "×":
                if first * second >= 0:
                    self.result = mt.log(first * second)
                else:
                    raise ValueError
            elif sign == "^":
                if first ** second >= 0:
                    self.result = mt.log(first ** second)
                else:
                    raise ValueError
            elif sign == "%":
                if first / 100 * second >= 0:
                    self.result = mt.log(first / 100 * second)
                else:
                    raise ValueError

# ---------------------------------- log ---------------------------------------
        elif self.mode[index] == "log":
            if first == "π":
                first = mt.pi
            elif first == "e":
                first = mt.e
            else:
                first = float(first)

            if second == "π":
                second = mt.pi
            elif second == "e":
                second = mt.e
            else:
                second = float(second)

            if sign == "+":
                if first + second >= 0:
                    self.result = mt.log10(first + second)
                else:
                    raise ValueError
            elif sign == "-":
                if first - second >= 0:
                    self.result = mt.log10(first - second)
                else:
                    raise ValueError
            elif sign == "/":
                if first / second >= 0:
                    self.result = mt.log10(first / second)
                else:
                    raise ValueError
            elif sign == "×":
                if first * second >= 0:
                    self.result = mt.log10(first * second)
                else:
                    raise ValueError
            elif sign == "^":
                if first ** second >= 0:
                    self.result = mt.log10(first ** second)
                else:
                    raise ValueError
            elif sign == "%":
                if first / 100 * second >= 0:
                    self.result = mt.log10(first / 100 * second)
                else:
                    raise ValueError

# ----------------------------- TAN -------------------------------------------
        elif self.mode[index] == "tan":
            if not self.inv:
                if self.rad:
                    if not flag[0] and not flag[1]:
                        if sign == "+":
                            self.result = mt.tan(float(first) + float(second))
                        elif sign == "-":
                            self.result = mt.tan(float(first) - float(second))
                        elif sign == "/":
                            if float(second) == 0.0:
                                raise ZeroDivisionError
                            else:
                                self.result = mt.tan(float(first) / float(second))
                        elif sign == "×":
                            self.result = mt.tan(float(first) * float(second))
                        elif sign == "^":
                            self.result = mt.tan(float(first) ** float(second))
                        elif sign == "%":
                            self.result = mt.tan(float(first) / 100 * float(second))
                    elif flag[0] and not flag[1]:
                        if first == "π":
                            first = mt.pi
                        elif first == "e":
                            first = mt.e
                        if sign == "+":
                            self.result = mt.tan(first + float(second))
                        elif sign == "-":
                            self.result = mt.tan(first - float(second))
                        elif sign == "/":
                            if float(second) == 0.0:
                                raise ZeroDivisionError
                            else:
                                self.result = mt.tan(first / float(second))
                        elif sign == "×":
                            self.result = mt.tan(first * float(second))
                        elif sign == "^":
                            self.result = mt.tan(first ** float(second))
                        elif sign == "%":
                            self.result = mt.tan(first / 100 * float(second))
                    elif not flag[0] and flag[1]:
                        if second == "π":
                            second = mt.pi
                        elif second == "e":
                            second = mt.e
                        if sign == "+":
                            self.result = mt.tan(float(first) + second)
                        elif sign == "-":
                            self.result = mt.tan(float(first) - second)
                        elif sign == "/":
                            self.result = mt.tan(float(first) / second)
                        elif sign == "×":
                            self.result = mt.tan(float(first) * second)
                        elif sign == "^":
                            self.result = mt.tan(float(first) ** second)
                        elif sign == "%":
                            self.result = mt.tan(float(first) / 100 * second)
                    elif flag[0] and flag[1]:
                        if first == "π":
                            first = mt.pi
                        elif first == "e":
                            first = mt.e
                        if second == "π":
                            second = mt.pi
                        elif second == "e":
                            second = mt.e
                        if sign == "+":
                            self.result = mt.tan(first + second)
                        elif sign == "-":
                            self.result = mt.tan(first - second)
                        elif sign == "/":
                            self.result = mt.tan(first / second)
                        elif sign == "×":
                            self.result = mt.tan(first * second)
                        elif sign == "^":
                            self.result = mt.tan(first ** second)
                        elif sign == "%":
                            self.result = mt.tan(first / 100 * second)
                elif not self.rad:
                    if not flag[0] and not flag[1]:
                        if sign == "+":
                            first = float(first) / 180 * mt.pi
                            second = float(second) / 180 * mt.pi
                            self.result = mt.tan(first + second)
                        elif sign == "-":
                            first = float(first) / 180 * mt.pi
                            second = float(second) / 180 * mt.pi
                            self.result = mt.tan(first - second)
                        elif sign == "/":
                            if float(second) == 0.0:
                                raise ZeroDivisionError
                            else:
                                first = (float(first) / float(second)) / 180 * mt.pi
                                self.result = mt.tan(first)
                        elif sign == "×":
                                first = (float(first) * float(second)) / 180 * mt.pi
                                self.result = mt.tan(first)
                        elif sign == "^":
                                first = (float(first) ** float(second)) / 180 * mt.pi
                                self.result = mt.tan(first)
                        elif sign == "%":
                                first = (float(first) / 100 * float(second)) / 180 * mt.pi
                                self.result = mt.tan(first)
                    elif flag[0] and not flag[1]:
                        if first == "π":
                            first = 180
                        elif first == "e":
                            first = mt.e
                        if sign == "+":
                            second = float(second) / 180 * mt.pi
                            self.result = mt.tan(first + second)
                        elif sign == "-":
                            second = float(second) / 180 * mt.pi
                            self.result = mt.tan(first - second)
                        elif sign == "/":
                            if float(second) == 0.0:
                                raise ZeroDivisionError
                            else:
                                first = (first / float(second)) / 180 * mt.pi
                                self.result = mt.tan(first / second)
                        elif sign == "×":
                            first = (first * float(second)) / 180 * mt.pi
                            self.result = mt.tan(first * second)
                        elif sign == "^":
                            first = (first ** float(second)) / 180 * mt.pi
                            self.result = mt.tan(first ** second)
                        elif sign == "%":
                            first = (first / 100 * float(second)) / 180 * mt.pi
                            self.result = mt.tan(first / 100 * second)
                    elif not flag[0] and flag[1]:
                        if second == "π":
                            second = 180
                        elif second == "e":
                            second = mt.e
                        if sign == "+":
                            first = float(first) / 180 * mt.pi
                            self.result = mt.tan(first + second)
                        elif sign == "-":
                            first = float(first) / 180 * mt.pi
                            self.result = mt.tan(first - second)
                        elif sign == "/":
                            first = (float(first) / second) / 180 * mt.pi
                            self.result = mt.tan(first / second)
                        elif sign == "×":
                            first = (float(first) * second) / 180 * mt.pi
                            self.result = mt.tan(first * second)
                        elif sign == "^":
                            first = (float(first) ** second) / 180 * mt.pi
                            self.result = mt.tan(first ** second)
                        elif sign == "%":
                            first = (float(first) / 100 * second) / 180 * mt.pi
                            self.result = mt.tan(first / 100 * second)
                    elif flag[0] and flag[1]:
                        if first == "π":
                            first = 180
                        elif first == "e":
                            first = mt.e
                        if second == "π":
                            second = 180
                        elif second == "e":
                            second = mt.e
                        if sign == "+":
                            first = (first + second) / 180 * mt.pi
                            self.result = mt.tan(first)
                        elif sign == "-":
                            first = (first - second) / 180 * mt.pi
                            self.result = mt.tan(first - second)
                        elif sign == "/":
                            first = (first / second) / 180 * mt.pi
                            self.result = mt.tan(first)
                        elif sign == "×":
                            first = (first * second) / 180 * mt.pi
                            self.result = mt.tan(first)
                        elif sign == "^":
                            first = (first ** second) / 180 * mt.pi
                            self.result = mt.tan(first)
                        elif sign == "%":
                            first = (first / 100 * second) / 180 * mt.pi
                            self.result = mt.tan(first)
            elif self.inv:
                if self.rad:
                    if first == "π":
                        first = mt.pi
                    elif first == "e":
                        first = mt.e
                    else:
                        first = float(first)

                    if second == "π":
                        second = mt.pi
                    elif second == "e":
                        second = mt.e
                    else:
                        second = float(second)

                    if sign == "+":
                        self.result = mt.atan(first + second)
                    elif sign == "-":
                        self.result = mt.atan(first - second)
                    elif sign == "/":
                        if second != 0.0:
                            self.result = mt.atan(first / second)
                        else:
                            raise ValueError
                    elif sign == "×":
                        self.result = mt.atan(first * second)
                    elif sign == "^":
                        self.result = mt.atan(first ** second)
                    elif sign == "%":
                        self.result = mt.atan(first / 100 * second)

                elif not self.rad:
                    if first == "π":
                        first = mt.pi
                    elif first == "e":
                        first = mt.e
                    else:
                        first = float(first)

                    if second == "π":
                        second = mt.pi
                    elif second == "e":
                        second = mt.e
                    else:
                        second = float(second)
                    if sign == "+":
                        self.result = mt.atan(first + second)
                        self.result = self.result / mt.pi * 180
                    elif sign == "-":
                        self.result = mt.atan(first - second)
                        self.result = self.result / mt.pi * 180
                    elif sign == "/":
                        if second != 0.0:
                            self.result = mt.atan(first / second)
                            self.result = self.result / mt.pi * 180
                        else:
                            raise ValueError
                    elif sign == "×":
                        self.result = mt.atan(first * second)
                        self.result = self.result / mt.pi * 180
                    elif sign == "^":
                        self.result = mt.atan(first ** second)
                        self.result = self.result / mt.pi * 180
                    elif sign == "%":
                        self.result = mt.atan(first / 100 * second)
                        self.result = self.result / mt.pi * 180
        print("result in calculate", self.result)
        return self.result


class OneShot:

    def __init__(self, expression=None):
        self.expression = expression
        bracket = BracketPair(expression=self.expression)
        self.bracket_pair = bracket.pair()

    def one(self):
        mode_list = list()
        if not self.bracket_pair:
            print("Bracket Error in one shot")
        else:
            mode_list = ["default"] * len(self.bracket_pair)

            for index, items in enumerate(self.bracket_pair):
                sign = []
                sign_hit = False
                i = items[0]
                if items[1] == len(self.expression) - 1:
                    pass
                else:
                    if self.expression[items[1] + 1] == "!":
                        mode_list[index] = "Double"
                while not sign_hit:
                    i -= 1
                    if self.expression[i] == "+" or self.expression[i] == "-" or self.expression[i] == "/" or self.expression[i] == "×" or self.expression[i] == "^" or self.expression[i] == "(":
                        sign_hit = True
                    else:
                        sign.append(self.expression[i])
                sign.reverse()
                sign = "".join(sign)
                if sign == "sqrt":
                    mode_list[index] = "sqrt"
                elif sign == "sin":
                    mode_list[index] = "sin"
                elif sign == "cos":
                    mode_list[index] = "cos"
                elif sign == "tan":
                    mode_list[index] = "tan"
                elif sign == "asin":
                    mode_list[index] = "asin"
                elif sign == "acos":
                    mode_list[index] = "acos"
                elif sign == "atan":
                    mode_list[index] = "atan"
                elif sign == "ln":
                    mode_list[index] = "ln"
                elif sign == "log":
                    mode_list[index] = "log"
            return mode_list.copy()


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
                            enter_br = True
                        elif a[idx + count] == "(":
                            enter_count -= 1
                        elif a[idx + count] == ")" and close_count == 0:
                            ini_enter_br = True
                            # print("here")
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

class SignPriority:

    def __init__(self, expression = None, brackets_list = None):
        self.expression = expression
        self.brackets_list = brackets_list
        self.s_list = [["!", "!"], ["^", "^"],["×", "/"],["%", "%"], ["+", "-"]]

    def sign(self, bracket_index = None):
        bracket_list = self.brackets_list[bracket_index]
        sign_list = []
        for i in range(len(self.s_list)):
            bracket_hit = 0
            index = bracket_list[0] + 1
            while index < bracket_list[1]:
                char = self.expression[index]
                if bracket_hit > 0:
                    if char == ")":
                        bracket_hit -= 1
                    elif char == "(":
                        bracket_hit += 1
                    else:
                        pass
                else:
                    if char == "(":
                        bracket_hit += 1
                    else:
                        if char.isdigit():
                            pass
                        else:
                            if char == self.s_list[i][0]:
                                sign_list.append(char)
                            elif char == self.s_list[i][1]:
                                sign_list.append(char)
                            else:
                                pass
                index += 1
        if len(sign_list) == 0:
            return False
        else:
            return sign_list.copy()

class BracketPair:

    def __init__(self, expression = None):
        self.expression = expression

    def pair(self):
        inv_expression = self.expression[::-1]
        length = len(self.expression)
        bracket_enter = True
        bracket_close = True
        index = 0
        index_len = 0
        brackets_enter = list()
        brackets_close = list()
        while bracket_enter:
            index = self.expression[index:length].find("(")
            if index != -1:
                index = index_len + index + 1
                index_len = index
                brackets_enter.append(index-1)
            else:
                bracket_enter = False
        index = 0
        index_len = 0
        while bracket_close:
            index = inv_expression[index:length].find(")")
            if index != -1:
                index = index_len + index + 1
                index_len = index
                brackets_close.append(length - index)
            else:
                bracket_close = False
        brackets_enter = brackets_enter[::-1]
        x = len(brackets_close)
        y = len(brackets_enter)
        if x == y:
            enter_paired = list()
            close_paired = list()
            brackets_pair = list()
            loop = 0
            enter_paired = [False] * x
            close_paired = [False] * x
            for index, item in enumerate(brackets_enter):
                loop += 1
                count = 0
                num = 0
                for idx, itm in enumerate(brackets_close):
                    num += 1
                    if item < itm and num < x:
                        pass
                    elif item > itm:
                        num = 0
                        while enter_paired[index] == False:
                            count += 1
                            if close_paired[idx - count]:
                                pass
                            else:
                                brackets_pair.append([item, brackets_close[idx - count]])
                                close_paired[idx - count] = True
                                enter_paired[index] = True
                    elif num == x:
                        num = 0
                        while enter_paired[index] == False:
                            if close_paired[idx - count]:
                                pass
                            else:
                                brackets_pair.append([item, brackets_close[idx - count]])
                                close_paired[idx - count] = True
                                enter_paired[index] = True
                            count += 1
            return brackets_pair.copy()
        else:
            return False

class Calculate:

    def __init__(self, expression=None, rad=True, inv=False):
        self.expression = expression
        self.rad = rad
        self.inv = inv
        self.mode_list = list()
        self.bracket_list = list()
        self.bracket_value = list()
        self.pair_change = list()
        self.calculated = list()
        self.result = 0
        self.pi_e_flag = [False, False]
        self.single_flag = False
        self.expression, self.mode_list, self.bracket_list = self.prepare()
        print(self.expression)
        print(self.bracket_list)
        print(self.mode_list)
        if not self.bracket_list[0]:
            self.result = None
        else:
            for item in range(len(self.bracket_list)):
                self.bracket_value.append(None)
            for item in range(len(self.expression)):
                self.calculated.append([False, None])
            self.au = ArithmeticUnit(rad=self.rad, inv=self.inv, mode=self.mode_list)
            self.sign_parse()

    def __del__(self):
        pass

    def get_result(self):
        return self.result

    def prepare(self):
        """Илэрхийллйиг Calculate клас ашиглахад зориулж янзална"""
        x = list(self.expression)
        is_space = True
        while is_space:
            for item in x:
                if item == " ":
                    x.remove(" ")
                    is_space = True
                    break
                else:
                    is_space = False
            continue
        result = "".join(x)
        insrt = Insert(expression=result)
        result = insrt.cross()
        del insrt
        insrt = Insert(expression=result)
        result = insrt.pow_bracket()
        del insrt
        insrt = Insert(expression=result)
        result = insrt.bracket()
        del insrt
        insrt = Insert(expression=result)
        result = insrt.zero()
        del insrt
        insrt = Insert(expression=result)
        result = insrt.fact_bracket()
        del insrt
        shot = OneShot(expression=result)
        mode_list = shot.one()
        del shot
        bracket = BracketPair(expression=result)
        bracket_list = bracket.pair()
        print(result)
        print(mode_list)
        print(bracket_list)
        if not bracket_list:
            bracket_list = [False]
        else:
            return result, mode_list.copy(), bracket_list.copy()

    def one_argument_parser(self, idx, br_enter, br_close, rng):
        """1 аргумент авдаг функц бүхий үйлдэл гүйцэтгэнэ"""
        value = list()
        for i in range(rng):
            if self.expression[br_enter + i].isdigit():
                value.append(self.expression[br_enter + i])
            elif self.expression[br_enter + i] == "π" or self.expression[br_enter + i] == "e":
                self.single_flag = True
                value.append(self.expression[br_enter + i])
            elif self.expression[br_enter + i] == "(":
                for ind, item in enumerate(self.bracket_list):
                        if item[0] == br_enter + i:
                            value.append(str(self.bracket_value[ind]))
                            break
                break
            else:
                pass
            continue
        single_value = "".join(value)
        result = self.au.singleInput(self.single_flag, single_value, idx)
        self.bracket_value[idx] = result
        self.result = result

    def two_argument_parser(self, indexs, sign_index, sign):
        """2 аргумент авдаг функц бүхий үйлдэл гүйцэтгэнэ"""
        value = list()
        first = ""
        second = ""
        first_value = None
        second_value = None
        sign_hit = False
        idx = sign_index
        value_hold_index = list()
        bracket_val_change = None
        while not sign_hit:
            idx -= 1
            if not self.calculated[idx][0]:
                if self.expression[idx].isdigit() or self.expression[idx] == ".":
                    value.append(self.expression[idx])
                    value_hold_index.append(idx)
                elif self.expression[idx] == "π" or self.expression[idx] == "e":
                    value.append(self.expression[idx])
                    value_hold_index.append(idx)
                    sign_hit = True
                    self.pi_e_flag[0] = True
                    self.calculated[idx][0] = True
                elif self.expression[idx] == ")":
                    for ind, item in enumerate(self.bracket_list):
                        if item[1] == idx:
                            first_value = self.bracket_value[ind]
                            sign_hit = True
                else:
                    sign_hit = True
            else:
                first_value = self.calculated[idx][1]
                sign_hit = True
        value.reverse()
        first = "".join(value)
        value.clear()
        if first_value == None:
            first_value = first
        else:
            pass
        sign_hit = False
        idx = sign_index
        while not sign_hit:
            idx += 1
            if not self.calculated[idx][0]:
                if self.expression[idx].isdigit() or self.expression[idx] == ".":
                    value.append(self.expression[idx])
                    value_hold_index.append(idx)
                    self.calculated[idx][0] = True
                elif self.expression[idx] == "π" or self.expression[idx] == "e":
                    value.append(self.expression[idx])
                    value_hold_index.append(idx)
                    sign_hit = True
                    self.calculated[idx][0] = True
                    self.pi_e_flag[1] = True
                elif self.expression[idx] == "(":
                    for ind, item in enumerate(self.bracket_list):
                        if item[0] == idx:
                            second_value = self.bracket_value[ind]
                            sign_hit = True
                            bracket_val_change = ind
                elif self.expression[idx] == "+" or self.expression[idx] == "-" or self.expression[idx] == ")":
                    sign_hit = True
                else:
                    pass
            else:
                second_value = self.calculated[idx][1]
                sign_hit = True
        second = second.join(value)
        value.clear()
        if second_value == None:
            second_value = second
        else:
            pass
        result = self.au.doubleInput(self.pi_e_flag ,first_value, second_value, indexs, sign)
        self.bracket_value[indexs] = result
        self.result = result
        for index in value_hold_index:
            self.calculated[index][1] = result
            self.calculated[index][0] = True
        if bracket_val_change != None:
            self.bracket_value[bracket_val_change] = result
        else:
            pass

    def fact_pars(self, bracket_index, sign_index):
        print(self.single_flag)
        value_found = False
        value_list = list()
        dr = False
        while not value_found:
            sign_index -= 1
            if self.expression[sign_index] == ")":
                for idx, item in enumerate(self.bracket_list):
                    if item[1] == sign_index:
                        value = str(self.bracket_value[idx])
                        value_found = True
                        dr = True
            elif self.expression[sign_index] == "π" or self.expression[sign_index] == "e":
                self.single_flag = True
                value = self.expression[sign_index]
                dr = True
                value_found = True
            elif self.expression[sign_index].isdigit() or self.expression == ".":
                value_list.append(self.expression[sign_index])
            elif self.expression[sign_index] == "(":
                value_found = True
            else:
                value_found = True
        if dr:
            result = self.au.fact_calculate(self.single_flag, value)
            self.bracket_value[bracket_index] = result
            self.result = result
            print(self.result)
        else:
            value_list.reverse()
            value = "".join(value_list)
            result = self.au.fact_calculate(self.single_flag, value)
            self.bracket_value[bracket_index] = result
            self.result = result
            print(self.result)

    def sign_parse(self):
        signs = SignPriority(expression=self.expression, brackets_list=self.bracket_list)
        for idx, item in enumerate(self.bracket_list):
            sign_list = signs.sign(bracket_index=idx)
            enter_index = item[0] + 1
            close_index = item[1] - 1
            rang = item[1] - item[0] - 1
            print(sign_list)
            if not sign_list:
                self.one_argument_parser(idx, enter_index, close_index, rang)
            else:
                for sign in sign_list:
                    for i in range(rang):
                        if self.expression[i + enter_index] == sign:
                            if sign == "!":
                                self.fact_pars(idx, i + enter_index)
                                b = list(self.expression)
                                b[i + enter_index] = "$"
                                self.expression = "".join(b)
                            else:
                                self.two_argument_parser(idx, i + enter_index, sign)
                                b = list(self.expression)
                                b[i + enter_index] = "$"
                                self.expression = "".join(b)


expression = "ln(e^2)"
try:
    calc = Calculate(expression=expression, rad=False, inv=False)
    result = round(calc.get_result(), 10)
    print("final result ", result)
except ValueError as error:
    print("Wrong input")
