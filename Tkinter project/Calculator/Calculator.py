import math as mt
from tkinter import Tk
from tkinter import Message
from tkinter import Entry
from tkinter import Label
from tkinter import LabelFrame
from tkinter import Button
from tkinter import Menu
from tkinter import Text
from tkinter import INSERT
from tkinter import END
from tkinter import SUNKEN
from tkinter import StringVar
from tkinter import IntVar
from tkinter import ttk
from tkinter import Frame
from tkinter import Toplevel
# ---------------------------------------------------------------------------


class Convert:

    def __init__(self, val=None):
        self.val = val
        self.hex_val = {
            "0": "0000",
            "1": "0001",
            "2": "0010",
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
            "a": "1010",
            "b": "1011",
            "c": "1100",
            "d": "1101",
            "e": "1110",
            "f": "1111"
        }
        self.octal_val = {
            "0": "000",
            "1": "001",
            "2": "010",
            "3": '011',
            "4": "100",
            "5": "101",
            "6": "110",
            "7": "111"
        }

    def hex_converter(self):
        x = list(self.val)
        new = list()
        for item in x:
            new.append(self.hex_val.get(item, "2"))
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
                raise ValueError
            r -= 1
        if is_valid:
            res.append(u)
            res.append(bin(u))
            res.append(oct(u))
            res.append(hex(u))
            return res
        else:
            return False

    def octal_converter(self):
        x = list(self.val)
        new = list()
        for item in x:
            new.append(self.octal_val.get(item, "2"))
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
                raise ValueError
            r -= 1
        if is_valid:
            res.append(u)
            res.append(bin(u))
            res.append(oct(u))
            res.append(hex(u))
            return res.copy()
        else:
            return False

    def binary_converter(self):
        res = list()
        is_valid = True
        t = self.val
        lst = [int(q) for q in str(t)]
        u = 0
        r = len(lst) - 1
        for i in range(0, len(lst)):
            if lst[i] == 1:
                u = u + pow(2, r)
            elif lst[i] == 0:
                pass
            else:
                raise ValueError
            r -= 1
        if is_valid:
            res.append(u)
            res.append(bin(u))
            res.append(oct(u))
            res.append(hex(u))
            return res.copy()
        else:
            return False

    def decimal_converter(self):
        res = list()
        res.append(self.val)
        res.append(bin(int(self.val)))
        res.append(oct(int(self.val)))
        res.append(hex(int(self.val)))
        return res.copy()


class DataConverter(Tk):

    def __init__(self, master):
        self.master = master
        self.__options = ["DEC", "BIN", "OCT", "HEX"]
        self._selected = StringVar()
        self.__input = 0
        self.window = Toplevel(self.master)
        self.window.resizable(False, False)
        self.frame1 = ttk.LabelFrame(self.window, text="Input")
        self.frame1.pack(fill="x")
        self.menu = ttk.Combobox(self.frame1, value=self.__options, textvariable=self._selected)
        self.menu.current(0)
        self.menu.config(state="readonly", width=4)
        self.menu.bind("<<ComboboxSelected>>")
        self.menu.grid(row=0, column=0)
        self.entr = ttk.Entry(self.frame1, font=("default", 10), width=50)
        self.entr.grid(row=0, column=1, columnspan=2)
        self.btn = ttk.Button(self.frame1, text="Convert", command=self.check)
        self.btn.grid(row=1, column=2)
        self.btn_clr = ttk.Button(self.frame1, text="Clear", command=self.clear)
        self.btn_clr.grid(row=1, column=1)
        self.frame2 = ttk.LabelFrame(self.window, text="Result")
        self.frame2.pack(fill="x")
        self.label1 = ttk.Label(self.frame2, text="BIN")
        self.label1.grid(row=0, column=0)
        self.entr1 = ttk.Entry(self.frame2, font=("default", 10), state="readonly", width=50)
        self.entr1.grid(row=0, column=1, pady=5, sticky="w")
        self.label2 = ttk.Label(self.frame2, text="OCT")
        self.label2.grid(row=1, column=0)
        self.entr2 = ttk.Entry(self.frame2, font=("default", 10), state="readonly", width=50)
        self.entr2.grid(row=1, column=1, pady=5, sticky="w")
        self.label3 = ttk.Label(self.frame2, text="DEC")
        self.label3.grid(row=2, column=0)
        self.entr3 = ttk.Entry(self.frame2, font=("default", 10), state="readonly", width=50)
        self.entr3.grid(row=2, column=1, pady=5, sticky="w")
        self.label4 = ttk.Label(self.frame2, text="HEX")
        self.label4.grid(row=3, column=0)
        self.entr4 = ttk.Entry(self.frame2, font=("default", 10), state="readonly", width=50)
        self.entr4.grid(row=3, column=1, pady=5, sticky="w")

    def check(self):
        result = list()
        a = self._selected.get()
        self.__input = self.entr.get()
        crt = Convert(val=self.__input)
        try:
            if a == "BIN":
                result = crt.binary_converter()
            elif a == "OCT":
                result = crt.octal_converter()
            elif a == "DEC":
                result = crt.decimal_converter()
            elif a == "HEX":
                result = crt.hex_converter()
        except ValueError:
            self.entr.delete(0, END)
            self.entr.insert(0, "# INVALID_VALUE #")
            result = ["#", "0x#", "0x#", "0x#"]
        self.entr1.config(state="normal")
        self.entr2.config(state="normal")
        self.entr3.config(state="normal")
        self.entr4.config(state="normal")
        self.entr1.delete(0, END)
        self.entr2.delete(0, END)
        self.entr3.delete(0, END)
        self.entr4.delete(0, END)
        self.entr1.insert(0, result[1][2:])
        self.entr2.insert(0, result[2][2:])
        self.entr3.insert(0, result[0])
        self.entr4.insert(0, result[3][2:].upper())
        self.entr1.config(state="readonly")
        self.entr2.config(state="readonly")
        self.entr3.config(state="readonly")
        self.entr4.config(state="readonly")

    def clear(self):
        self.entr1.config(state="normal")
        self.entr2.config(state="normal")
        self.entr3.config(state="normal")
        self.entr4.config(state="normal")
        self.entr.delete(0, END)
        self.entr1.delete(0, END)
        self.entr2.delete(0, END)
        self.entr3.delete(0, END)
        self.entr4.delete(0, END)
        self.entr1.config(state="readonly")
        self.entr2.config(state="readonly")
        self.entr3.config(state="readonly")
        self.entr4.config(state="readonly")

# ---------------------------------------------------->
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
        return self.result

    def fact_calculate(self, flag=False, value=None):
        if flag:
            raise ValueError
        else:
            val = float(value)
            if val - round(val) < 0.00000000000001:
                self.result = mt.factorial(round(val))
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
                        if sign == "+":
                            first = float(first) / 180 * mt.pi
                            second = float(second) / 180 * mt.pi
                            self.result = mt.sin(first + second)
                        elif sign == "-":
                            first = float(first) / 180 * mt.pi
                            second = float(second) / 180 * mt.pi
                            self.result = mt.sin(first - second)
                        elif sign == "/":
                            if float(second) == 0.0:
                                raise ZeroDivisionError
                            else:
                                first = (float(first) / float(second)) / 180 * mt.pi
                                self.result = mt.sin(first)
                        elif sign == "×":
                            first = (float(first) * float(second)) / 180 * mt.pi
                            self.result = mt.sin(first)
                        elif sign == "^":
                            first = (float(first) ** float(second)) / 180 * mt.pi
                            self.result = mt.sin(first)
                        elif sign == "%":
                            first = (float(first) / 100 * float(second)) / 180 * mt.pi
                            self.result = mt.sin(first)
                    elif flag[0] and not flag[1]:
                        if first == "π":
                            first = 180
                        elif first == "e":
                            first = mt.e
                        if sign == "+":
                            second = float(second) / 180 * mt.pi
                            self.result = mt.sin(first + second)
                        elif sign == "-":
                            second = float(second) / 180 * mt.pi
                            self.result = mt.sin(first - second)
                        elif sign == "/":
                            if second == 0.0:
                                raise ZeroDivisionError
                            else:
                                first = (first / float(second)) / 180 * mt.pi
                                self.result = mt.sin(first)
                        elif sign == "×":
                            first = (first * float(second)) / 180 * mt.pi
                            self.result = mt.sin(first)
                        elif sign == "^":
                            first = (first ** float(second)) / 180 * mt.pi
                            self.result = mt.sin(first)
                        elif sign == "%":
                            first = (first / 100 * float(second)) / 180 * mt.pi
                            self.result = mt.sin(first)
                    elif not flag[0] and flag[1]:
                        if second == "π":
                            second = 180
                        elif second == "e":
                            second = mt.e
                        if sign == "+":
                            first = float(first) / 180 * mt.pi
                            self.result = mt.sin(first + second)
                        elif sign == "-":
                            first = float(first) / 180 * mt.pi
                            self.result = mt.sin(first - second)
                        elif sign == "/":
                            first = float(first) / second
                            self.result = mt.sin(first)
                        elif sign == "×":
                            first = float(first) * second
                            self.result = mt.sin(first)
                        elif sign == "^":
                            first = float(first) ** second
                            self.result = mt.sin(first)
                        elif sign == "%":
                            first = float(first) / 100 * second
                            self.result = mt.sin(first)
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
                            self.result = mt.sin((first + second) / 180 * mt.pi)
                        elif sign == "-":
                            self.result = mt.sin((first - second) / 180 * mt.pi)
                        elif sign == "/":
                            self.result = mt.sin((first / second) / 180 * mt.pi)
                        elif sign == "×":
                            self.result = mt.sin((first * second) / 180 * mt.pi)
                        elif sign == "^":
                            self.result = mt.sin((first ** second) / 180 * mt.pi)
                        elif sign == "%":
                            self.result = mt.sin((first / 100 * second) / 180 * mt.pi)
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

# --------------------------------------- sqrt --------------------------------
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

# ---------------------------------- log --------------------------------------
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
        return self.result


class OneShot:

    def __init__(self, expression=None):
        self.expression = expression
        bracket = BracketPair(expression=self.expression)
        self.bracket_pair = bracket.pair()

    def one(self):
        mode_list = list()
        if not self.bracket_pair:
            pass
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
                        mode_list[index] = "default"
                while not sign_hit:
                    i -= 1
                    if self.expression[i] == "+" or self.expression[i] == "-" or self.expression[i] == "/" or self.expression[i] == "×" or self.expression[i] == "^" or self.expression[i] == "(":
                        sign_hit = True
                    else:
                        sign.append(self.expression[i])
                sign.reverse()
                sign = "".join(sign)
                if sign == "√":
                    mode_list[index] = "sqrt"
                elif sign == "sin":
                    mode_list[index] = "sin"
                elif sign == "cos":
                    mode_list[index] = "cos"
                elif sign == "tan":
                    mode_list[index] = "tan"
                elif sign == "asin":
                    mode_list[index] = "sin"
                elif sign == "acos":
                    mode_list[index] = "cos"
                elif sign == "atan":
                    mode_list[index] = "tan"
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
                elif nxt == "e" or nxt == "π" and not last.isdigit():
                    a.insert(count + mul_count, "×")
                    mul_count += 1
                elif last.isdigit() and not nxt.isdigit():
                    a.insert(count + mul_count, "×")
                    mul_count += 1
                elif last == "e" or last == "π" and not nxt.isdigit():
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
        for index, item in enumerate(self.x):
            if item == "!":
                closed = False
                enter = False
                i = index
                a.insert(i + 1 + count, ")")
                if a[i - 1 + count] == ")":
                    enter = True
                else:
                    pass
                while not closed:
                    i -= 1
                    if enter:
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
                    else:
                        pass
            else:
                pass
        a = "".join(a)
        return a

    def pow_bracket(self):
        a = self.x.copy()
        count = 0
        for index, item in enumerate(self.x):
            if item == "^":
                idx = index
                bracket_hit = False
                bracket_close = False
                enter_count = 0
                while not bracket_close:
                    idx -= 1
                    if bracket_hit:
                        if a[idx + count] == "(" and idx + count == 0:
                            a.insert(0, "(")
                            count += 1
                            bracket_hit = False
                            bracket_close = True
                        elif a[idx + count] == "(":
                            enter_count -= 1
                            if enter_count == 0:
                                bracket_hit = False
                            else:
                                pass
                        elif a[idx + count] == ")":
                            enter_count += 1
                        else:
                            pass
                    else:
                        if idx + count == 0:
                            bracket_close = True
                            a.insert(0, "(")
                            count += 1
                        elif a[idx + count] == ")":
                            bracket_hit = True
                            enter_count += 1
                        elif a[idx + count] == "(" and enter_count == 0:
                            bracket_close = True
                            a.insert(idx + count + 1, "(")
                            count += 1
                        elif a[idx + count] == "+" or a[idx + count] == "-" or a[idx + count] == "^" or a[idx + count] == "%" or a[idx + count] == "/" or a[idx + count] == "×":
                            bracket_close = True
                            a.insert(idx + count + 1, "(")
                            count += 1
                        elif a[idx + count].isdigit() or a[idx + count] == "." or a[idx + count] or a[idx + count] == "e" or a[idx + count] == "π":
                            pass
                        elif a[idx + count] == "s" or a[idx + count] == "i" or a[idx + count] == "n" or a[idx + count] == "c" or a[idx + count] == "o" or a[idx + count] == "t" or a[idx + count] == "a":
                            pass
                        else:
                            bracket_close = True
                            a.insert(idx + count + 1, "(")
                            count += 1
                idx = index
                bracket_hit = False
                bracket_close = False
                enter_count = 0
                while not bracket_close:
                    idx += 1
                    if bracket_hit:
                        if a[idx + count] == ")" and idx + count == len(a):
                            a.insert(idx + count, ")")
                            count += 1
                            bracket_hit = False
                            bracket_close = True
                        elif a[idx + count] == ")":
                            enter_count -= 1
                            if enter_count == 0:
                                bracket_hit = False
                            else:
                                pass
                        elif a[idx + count] == "(":
                            enter_count += 1
                        else:
                            pass
                    else:
                        if idx + count == len(a):
                            bracket_close = True
                            a.insert(idx + count, ")")
                            count += 1
                        elif a[idx + count] == "(":
                            bracket_hit = True
                            enter_count += 1
                        elif a[idx + count] == ")" and enter_count == 0:
                            bracket_close = True
                            a.insert(idx + count, ")")
                            count += 1
                        elif a[idx + count] == "+" or a[idx + count] == "-" or a[idx + count] == "^" or a[idx + count] == "%" or a[idx + count] == "/" or a[idx + count] == "×":
                            bracket_close = True
                            a.insert(idx + count, ")")
                            count += 1
                        elif a[idx + count].isdigit() or a[idx + count] == "." or a[idx + count] or a[idx + count] == "e" or a[idx + count] == "π":
                            pass
                        elif a[idx + count] == "s" or a[idx + count] == "i" or a[idx + count] == "n" or a[idx + count] == "c" or a[idx + count] == "o" or a[idx + count] == "t" or a[idx + count] == "a":
                            pass
                        else:
                            bracket_close = True
                            a.insert(idx + count, ")")
                            count += 1
        a.insert(0, "(")
        a.insert(len(a), ")")
        a = "".join(a)
        return a

    def bracket(self):
        a = self.x.copy()
        count = 0
        for index, item in enumerate(self.x):
            if item == "×" or item == "/":
                idx = index
                bracket_hit = False
                bracket_close = False
                enter_count = 0
                while not bracket_close:
                    idx -= 1
                    if bracket_hit:
                        if a[idx + count] == "(" and idx + count == 0:
                            a.insert(0, "(")
                            count += 1
                            bracket_hit = False
                            bracket_close = True
                        elif a[idx + count] == "(":
                            enter_count -= 1
                            if enter_count == 0:
                                bracket_hit = False
                            else:
                                pass
                        elif a[idx + count] == ")":
                            enter_count += 1
                        else:
                            pass
                    else:
                        if idx + count == 0:
                            bracket_close = True
                            a.insert(0, "(")
                            count += 1
                        elif a[idx + count] == ")":
                            bracket_hit = True
                            enter_count += 1
                        elif a[idx + count] == "(" and enter_count == 0:
                            bracket_close = True
                            a.insert(idx + count + 1, "(")
                            count += 1
                        elif a[idx + count] == "+" or a[idx + count] == "-" or a[idx + count] == "^" or a[idx + count] == "%" or a[idx + count] == "/" or a[idx + count] == "×":
                            bracket_close = True
                            a.insert(idx + count + 1, "(")
                            count += 1
                        elif a[idx + count].isdigit() or a[idx + count] == "." or a[idx + count] or a[idx + count] == "e" or a[idx + count] == "π":
                            pass
                        elif a[idx + count] == "s" or a[idx + count] == "i" or a[idx + count] == "n" or a[idx + count] == "c" or a[idx + count] == "o" or a[idx + count] == "t" or a[idx + count] == "a":
                            pass
                        else:
                            bracket_close = True
                            a.insert(idx + count + 1, "(")
                            count += 1
                idx = index
                bracket_hit = False
                bracket_close = False
                enter_count = 0
                while not bracket_close:
                    idx += 1
                    if bracket_hit:
                        if a[idx + count] == ")" and idx + count == len(a):
                            a.insert(idx + count, ")")
                            count += 1
                            bracket_hit = False
                            bracket_close = True
                        elif a[idx + count] == ")":
                            enter_count -= 1
                            if enter_count == 0:
                                bracket_hit = False
                            else:
                                pass
                        elif a[idx + count] == "(":
                            enter_count += 1
                        else:
                            pass
                    else:
                        if idx + count == len(a):
                            bracket_close = True
                            a.insert(idx + count, ")")
                            count += 1
                        elif a[idx + count] == "(":
                            bracket_hit = True
                            enter_count += 1
                        elif a[idx + count] == ")" and enter_count == 0:
                            bracket_close = True
                            a.insert(idx + count, ")")
                            count += 1
                        elif a[idx + count] == "+" or a[idx + count] == "-" or a[idx + count] == "^" or a[idx + count] == "%" or a[idx + count] == "/" or a[idx + count] == "×":
                            bracket_close = True
                            a.insert(idx + count, ")")
                            count += 1
                        elif a[idx + count].isdigit() or a[idx + count] == "." or a[idx + count] or a[idx + count] == "e" or a[idx + count] == "π":
                            pass
                        elif a[idx + count] == "s" or a[idx + count] == "i" or a[idx + count] == "n" or a[idx + count] == "c" or a[idx + count] == "o" or a[idx + count] == "t" or a[idx + count] == "a":
                            pass
                        else:
                            bracket_close = True
                            a.insert(idx + count, ")")
                            count += 1
        a.insert(0, "(")
        a.insert(len(a), ")")
        a = "".join(a)
        return a


class SignPriority:

    def __init__(self, expression=None, brackets_list=None):
        self.expression = expression
        self.brackets_list = brackets_list
        self.s_list = [["!", "!"], ["^", "^"], ["×", "/"], ["%", "%"], ["+", "-"]]

    def sign(self, bracket_index=None):
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

    def __init__(self, expression=None):
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
                        while not enter_paired[index]:
                            count += 1
                            if close_paired[idx - count]:
                                pass
                            else:
                                brackets_pair.append([item, brackets_close[idx - count]])
                                close_paired[idx - count] = True
                                enter_paired[index] = True
                    elif num == x:
                        num = 0
                        while not enter_paired[index]:
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
        self.expression, self.mode_list, self.bracket_list = self.prepare()
        if not self.bracket_list[0]:
            self.result = None
        else:
            for _ in range(len(self.bracket_list)):
                self.bracket_value.append(None)
            for _ in range(len(self.expression)):
                self.calculated.append([False, None])
            self.au = ArithmeticUnit(rad=self.rad, inv=self.inv, mode=self.mode_list)
            self.sign_parse()

    def __del__(self):
        pass

    def prepare(self):
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
        if not bracket_list:
            bracket_list = [False]
        else:
            return result, mode_list.copy(), bracket_list.copy()

    def one_argument_parser(self, idx, br_enter, br_close, rng):
        value = list()
        single_flag = False
        for i in range(rng):
            if self.expression[br_enter + i].isdigit() or self.expression[br_enter + i] == ".":
                value.append(self.expression[br_enter + i])
            elif self.expression[br_enter + i] == "π" or self.expression[br_enter + i] == "e":
                single_flag = True
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
        result = self.au.singleInput(single_flag, single_value, idx)
        self.bracket_value[idx] = result
        self.result = result

    def two_argument_parser(self, indexs, sign_index, sign):
        """2 аргумент авдаг функц бүхий үйлдэл гүйцэтгэнэ"""
        value = list()
        first = ""
        second = ""
        pi_e_flag = [False, False]
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
                    pi_e_flag[0] = True
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
        if first_value is None:
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
                    pi_e_flag[1] = True
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
        if second_value is None:
            second_value = second
        else:
            pass
        result = self.au.doubleInput(pi_e_flag, first_value, second_value, indexs, sign)
        self.bracket_value[indexs] = result
        self.result = result
        for index in value_hold_index:
            self.calculated[index][1] = result
            self.calculated[index][0] = True
        if bracket_val_change is not None:
            self.bracket_value[bracket_val_change] = result
        else:
            pass

    def fact_pars(self, bracket_index, sign_index):
        value_found = False
        value_list = list()
        dr = False
        single_flag = False
        while not value_found:
            sign_index -= 1
            if self.expression[sign_index] == ")":
                for idx, item in enumerate(self.bracket_list):
                    if item[1] == sign_index:
                        value = str(self.bracket_value[idx])
                        value_found = True
                        dr = True
            elif self.expression[sign_index] == "π" or self.expression[sign_index] == "e":
                single_flag = True
                value = self.expression[sign_index]
                dr = True
                value_found = True
            elif self.expression[sign_index].isdigit() or self.expression[sign_index] == ".":
                value_list.append(self.expression[sign_index])
            elif self.expression[sign_index] == "(":
                value_found = True
            else:
                value_found = True
        if dr:
            result = self.au.fact_calculate(value=value)
            self.bracket_value[bracket_index] = result
            self.result = result
        else:
            value_list.reverse()
            value = "".join(value_list)
            result = self.au.fact_calculate(single_flag, value)
            self.bracket_value[bracket_index] = result
            self.result = result

    def sign_parse(self):
        signs = SignPriority(expression=self.expression, brackets_list=self.bracket_list)
        for idx, item in enumerate(self.bracket_list):
            sign_list = signs.sign(bracket_index=idx)
            enter_index = item[0] + 1
            close_index = item[1] - 1
            rang = item[1] - item[0] - 1
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


class About:

    def __init__(self):
        self.root = Tk()
        self.root.title("About")
        self.root.resizable(0, 0)
        self.root.config(bg="#D7D7D7")
        self.root.attributes("-toolwindow", 1)

    def display(self):
        name = Label(self.root, text="""
Calculator""", font=("consolas", 20, "bold"), padx=43)
        name.pack()
        label = Label(self.root, text="""----------------
Version -- 2.0
Created by Gantulga G
        """, borderwidth=10, padx=50)
        label.pack()
        self.root.mainloop()

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------


DOT = True
RND = 10
INV = False
RAD = True


def numberConverter():
    DataConverter(root)


def about():
    dis = About()
    dis.display()


def clear():
    entry.delete(0, END)
    label.config(state="normal")
    label.delete(0, END)
    label.config(state="readonly")


def clear_entry():
    val = entry.get()
    entry.delete(len(val) - 1, END)


def invert():
    global INV
    if not INV:
        btn_cos['text'] = "ACOS"
        btn_sin['text'] = "ASIN"
        btn_tan['text'] = "ATAN"
        btn_ln['text'] = "e^"
        btn_log['text'] = "10^"
        btn_sqrt['text'] = "^2"
        INV = True
        btn_inv['style'] = "Red.TButton"
    else:
        btn_cos['text'] = "COS"
        btn_sin['text'] = "SIN"
        btn_tan['text'] = "TAN"
        btn_ln['text'] = "ln"
        btn_log['text'] = "log"
        btn_sqrt['text'] = "sqrt"
        INV = False
        btn_inv['style'] = "Black.TButton"


def sin_cos_tan(val):
    global INV
    global RAD
    if not INV:
        entry.insert(INSERT, val)
    else:
        if val == "sin(":
            entry.insert(INSERT, "asin(")
        elif val == "cos(":
            entry.insert(INSERT, "acos(")
        elif val == "tan(":
            entry.insert(INSERT, "atan(")
    label['text'] = ""


def ln_log_sqrt(val):
    global INV
    if not INV:
        entry.insert(INSERT, val)
        label['text'] = ""
    else:
        if val == "ln(":
            entry.insert(INSERT, "e^")
            label['text'] = ""
        elif val == "log(":
            entry.insert(INSERT, "10^")
            label['text'] = ""
        elif val == "√(":
            entry.insert(INSERT, "^2")
            show()


def btn_rad():
    global RAD
    if btn_rad['text'] == "DEG":
        btn_rad['text'] = "RAD"
        RAD = True
    else:
        btn_rad['text'] = "DEG"
        RAD = False


def insert_val(val):
    entry.insert(INSERT, str(val))
    result = calculate()
    label.config(state="normal")
    last = label.get()
    if result == "0":
        pass
    elif result == "value":
        pass
    else:
        if len(last) > 0:
            label.delete(0, END)
            label.insert(0, f"{result}")
            label.config(state="readonly")
        else:
            label.insert(0, f"{result}")
            label.config(state="readonly")


def insert_sign(val):
    current = str(entry.get())
    if val == ".":
        if current.find(".") > -1:
            pass
        else:
            entry.insert(INSERT, val)
    else:
        entry.insert(INSERT, val)


def calculate():
    global RAD
    global INV
    global RND
    expression = entry.get()
    try:
        calc = Calculate(expression=expression, rad=RAD, inv=INV)
        result = round(calc.result, RND)
        del calc
    except ValueError:
        result = "Invalid input"
    except TypeError:
        result = "Invalid input"
    except IndexError:
        result = "Invalid input"
    except ZeroDivisionError:
        result = "Zero division"
    except OverflowError:
        result = "Result number too large"
    return result


def show():
    result = calculate()
    label.config(state="normal")
    label.delete(0, END)
    label.insert(0, f"{result}")
    label.config(state="readonly")


# root.geometry("400x400")
root = Tk()
root.title("Calculator")
root.resizable(False, False)
entry = ttk.Entry(root, width=20, font=("default", 15))
entry.grid(row=0, column=0, columnspan=2)
# root.config(bg="#FFFFFF")
label = ttk.Entry(root, width=20, font=("default", 15))
label.grid(row=1, column=0, columnspan=2)
label.config(state="readonly")
tools = ttk.LabelFrame(root)
tools.grid(row=2, column=0, columnspan=1)

s = ttk.Style(tools)
s.configure("Red.TButton", foreground='red')
b = ttk.Style(tools)
s.configure("Black.TButton", foreground='black')

btn_inv = ttk.Button(tools, text="INV", width=6, style="Black.TButton", command=invert)
btn_rad = ttk.Button(tools, text="RAD",  width=6, command=btn_rad)
btn_sin = ttk.Button(tools, text="SIN",  width=6, command=lambda: sin_cos_tan("sin("))
btn_cos = ttk.Button(tools, text="COS",  width=6, command=lambda: sin_cos_tan("cos("))
btn_tan = ttk.Button(tools, text="TAN",  width=6, command=lambda: sin_cos_tan("tan("))
btn_per = ttk.Button(tools, text="%",  width=6, command=lambda: insert_sign("%"))   
btn_ln = ttk.Button(tools, text="ln",  width=6, command=lambda: ln_log_sqrt("ln("))
btn_log = ttk.Button(tools, text="log",  width=6, command=lambda: ln_log_sqrt("log("))
btn_sqrt = ttk.Button(tools, text="√",  width=6, command=lambda: ln_log_sqrt("√("))
btn_pow = ttk.Button(tools, text="^",  width=6, command=lambda: insert_sign("^"))
btn_pi = ttk.Button(tools, text="PI",  width=6, command=lambda: insert_val("π"))
btn_e = ttk.Button(tools, text="e",  width=6, command=lambda: insert_val("e"))
btn_bracket1 = ttk.Button(tools, text="(",  width=6, command=lambda: insert_sign("("))
btn_bracket2 = ttk.Button(tools, text=")",  width=6, command=lambda: insert_val(")"))
btn_fact = ttk.Button(tools, text="!", width=6, command=lambda: insert_val("!"))

btn_inv.grid(row=0, column=0)
btn_rad.grid(row=0, column=1)
btn_sin.grid(row=0, column=2)
btn_cos.grid(row=0, column=3)
btn_tan.grid(row=0, column=4)
btn_per.grid(row=1, column=0)
btn_ln.grid(row=1, column=1)
btn_log.grid(row=1, column=2)
btn_sqrt.grid(row=1, column=3)
btn_pow.grid(row=1, column=4)
btn_pi.grid(row=2, column=0)
btn_e.grid(row=2, column=1)
btn_bracket1.grid(row=2, column=2)
btn_bracket2.grid(row=2, column=3)
btn_fact.grid(row=2, column=4)

numbers = ttk.LabelFrame(root)
numbers.grid(row=3, column=0)
# #AA7639
btn_1 = ttk.Button(numbers, text="1", width=6, command=lambda: insert_val(1))
btn_2 = ttk.Button(numbers, text="2", width=6, command=lambda: insert_val(2))
btn_3 = ttk.Button(numbers, text="3", width=6, command=lambda: insert_val(3))
btn_4 = ttk.Button(numbers, text="4", width=6, command=lambda: insert_val(4))
btn_5 = ttk.Button(numbers, text="5", width=6, command=lambda: insert_val(5))
btn_6 = ttk.Button(numbers, text="6", width=6, command=lambda: insert_val(6))
btn_7 = ttk.Button(numbers, text="7", width=6, command=lambda: insert_val(7))
btn_8 = ttk.Button(numbers, text="8", width=6, command=lambda: insert_val(8))
btn_9 = ttk.Button(numbers, text="9", width=6, command=lambda: insert_val(9))
btn_0 = ttk.Button(numbers, text="0", width=6, command=lambda: insert_val(0))
btn_d = ttk.Button(numbers, text=".", width=6, command=lambda: insert_sign("."))
btn_q = ttk.Button(numbers, text=",", width=6, command=lambda: insert_sign(","))
btn_div = ttk.Button(numbers, text="/", width=6, command=lambda: insert_sign("/"))
btn_clr = ttk.Button(numbers, text="C", width=6, command=clear)
btn_mul = ttk.Button(numbers, text="×", width=6, command=lambda: insert_sign("×"))
btn_sub = ttk.Button(numbers, text="-", width=6, command=lambda: insert_sign("-"))
btn_add = ttk.Button(numbers, text="+", width=6, command=lambda: insert_sign("+"))
btn_equ = ttk.Button(numbers, text="=", width=6, command=show)
btn_cle = ttk.Button(numbers, text="<-", width=6, command=clear_entry)
# #c2c2a3
btn_1.grid(row=2, column=0)
btn_2.grid(row=2, column=1)
btn_3.grid(row=2, column=2)
btn_sub.grid(row=2, column=3)

btn_4.grid(row=1, column=0)
btn_5.grid(row=1, column=1)
btn_6.grid(row=1, column=2)
btn_mul.grid(row=1, column=3)
btn_clr.grid(row=1, column=4)

btn_7.grid(row=0, column=0)
btn_8.grid(row=0, column=1)
btn_9.grid(row=0, column=2)
btn_div.grid(row=0, column=3)
btn_cle.grid(row=0, column=4)

btn_0.grid(row=3, column=0)
btn_d.grid(row=3, column=1)
btn_q.grid(row=3, column=2)
btn_add.grid(row=3, column=3)
btn_equ.grid(row=3, column=4)
s = IntVar()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="---")
filemenu.add_command(label="Converter", command=numberConverter)
filemenu.add_separator()
filemenu.add_checkbutton(0, label="text", variable=s)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Tools", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)    
root.config(menu=menubar)
root.mainloop()
