# -------------------- import methods ---------------------------------
from tkinter import *

# import tkinter as tk

# ------------------- root methods ------------------------------------
root = Tk()
# win = tk.Tk()

# ------------------- Title methods -----------------------------------
# win.title("First GUI")
root.title("Title")


def ClickEvent():
    hello = "Hello " + e.get()
    my_label = Label(root, text=hello)
    my_label.pack()


# ---------------- non Resizable GUI ----------------------------------
# win.resizable(False, False)
root.resizable(True, False)

# ---------------- Widgets --------------------------------------------
# tk.[Widget name](root window, properties/configuration)
# frame = tk.Frame(win)
# frame.pack()
# tk.Label(frame, text="Label 1").pack()
# win.Button(win, text="Button").pack()


e = Entry(root, width=50, bg="grey", fg="white", borderwidth=10)
e.pack()
e.insert(0, "Enter your name :")

button = Button(root, text="Enter your name", padx=50, pady=50, state=DISABLED,
                command=ClickEvent, fg="black", bg="yellow")
button.pack()

# ----------- Grid system ---------------------------------------------
# label = Label(root, text="Label")
# label2 = Label(root, text="Label")
# label2.grid(row=0, column=0)
# label.grid(row=1, column=1)


# win.mainloop()
root.mainloop()
