from tkinter import Tk
from tkinter import Button
from tkinter import Label
from tkinter import Entry
from tkinter import INSERT
from tkinter import END


class Option(Tk):

    def __init__(self, screenName=None, baseName=None, className="Options",
                 useTk=1, sync=0, use=None):
        super().__init__(screenName=screenName, baseName=baseName,
                         className=className, useTk=useTk, sync=sync, use=use)


class Option2(Tk):

    def __init__(self, screenName=None, baseName=None,
                 useTk=1, sync=0, use=None):
        super().__init__(screenName=screenName, baseName=baseName,
                         useTk=useTk, sync=sync, use=use)
        self.btn = Button(self, text="GG")


op = Option()
op2 = Option2()

op2.btn.pack()

op.mainloop()
op2.mainloop()
