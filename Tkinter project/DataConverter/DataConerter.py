from tkinter import *
from tkinter import ttk
# ----------------------------------->


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
        }
        self.octal_val = {
            "0": "000",
            "1": "001",
            "2": "010",
            "3": '011',
            "4": "100",
            "5": "101",
            "6": "110",
            "7": "111",
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

    def decimal_converter(self):
        res = list()
        res.append(self.val)
        res.append(bin(int(self.val)))
        res.append(oct(int(self.val)))
        res.append(hex(int(self.val)))
        return res.copy()


class DataConverter(Tk):

    def __init__(self, screenName=None, baseName=None, useTk=1, sync=0, use=None):
        super().__init__(screenName=screenName, baseName=baseName, useTk=useTk, sync=sync, use=use)
        self.__options = ["DEC", "BIN", "OCT", "HEX"]
        self.__selected = StringVar()
        self.__input = 0

        def check(self):
            a = self.__selected.get()
            self.__input = entr.get()
            crt = Convert(val=self.__input)
            if a == "BIN":
                result = crt.binary_converter()
            elif a == "OCT":
                result = crt.octal_converter()
            elif a == "DEC":
                result = crt.decimal_converter()
            elif a == "HEX":
                result = crt.hex_converter()
            entr1.config(state="normal")
            entr2.config(state="normal")
            entr3.config(state="normal")
            entr4.config(state="normal")
            entr1.delete(0, END)
            entr2.delete(0, END)
            entr3.delete(0, END)
            entr4.delete(0, END)
            entr1.insert(0, result[1][2:])
            entr2.insert(0, result[2][2:])
            entr3.insert(0, result[0])
            entr4.insert(0, result[3][2:].upper())
            entr1.config(state="readonly")
            entr2.config(state="readonly")
            entr3.config(state="readonly")
            entr4.config(state="readonly")

        def clear(self):
            entr1.config(state="normal")
            entr2.config(state="normal")
            entr3.config(state="normal")
            entr4.config(state="normal")
            entr.delete(0, END)
            entr1.delete(0, END)
            entr2.delete(0, END)
            entr3.delete(0, END)
            entr4.delete(0, END)
            entr1.config(state="readonly")
            entr2.config(state="readonly")
            entr3.config(state="readonly")
            entr4.config(state="readonly")

        self.title("DC")
        self.iconbitmap(default='DC.ico')
        self.resizable(True, False)
        frame1 = ttk.LabelFrame(self, text="Input")
        frame1.pack(fill="x")
        menu = ttk.Combobox(frame1, value=self.__options, textvariable=self.__selected)
        menu.current(0)
        menu.config(state="readonly", width=4)
        menu.bind("<<ComboboxSelected>>")
        menu.grid(row=0, column=0)
        entr = ttk.Entry(frame1, font=("default", 10), width=50)
        entr.grid(row=0, column=1, columnspan=2)
        btn = ttk.Button(frame1, text="Convert", command=lambda: check(self))
        btn.grid(row=1, column=2)
        btn_clr = ttk.Button(frame1, text="Clear", command=lambda: clear(self))
        btn_clr.grid(row=1, column=1)

        frame2 = ttk.LabelFrame(self, text="Result")
        frame2.pack(fill="x")
        label1 = ttk.Label(frame2, text="BIN")
        label1.grid(row=0, column=0)
        entr1 = ttk.Entry(frame2, font=("default", 10), state="readonly", width=50)
        entr1.grid(row=0, column=1, pady = 5, sticky="w")
        label2 = ttk.Label(frame2, text="OCT")
        label2.grid(row=1, column=0)
        entr2 = ttk.Entry(frame2, font=("default", 10), state="readonly", width=50)
        entr2.grid(row=1, column=1, pady = 5, sticky="w")
        label3 = ttk.Label(frame2, text="DEC")
        label3.grid(row=2, column=0)
        entr3 = ttk.Entry(frame2, font=("default", 10), state="readonly", width=50)
        entr3.grid(row=2, column=1, pady = 5, sticky="w")
        label4 = ttk.Label(frame2, text="HEX")
        label4.grid(row=3, column=0)
        entr4 = ttk.Entry(frame2, font=("default", 10), state="readonly", width=50)
        entr4.grid(row=3, column=1, pady = 5, sticky="w")

        self.mainloop()
DataConverter()