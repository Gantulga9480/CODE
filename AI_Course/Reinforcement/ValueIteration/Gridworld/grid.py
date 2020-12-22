from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import numpy as np
import pygame
import os
import cv2
# import threading

import game as game
import game_util as util
import create as create
import play as play
import train as traine

pygame.init()
pygame.mixer.init()


class Input:

    def __init__(self, parent):
        self.top = Toplevel(parent)
        self.top.title("Enter env size")
        self.top.resizable(False, False)
        self.entry = ttk.Entry(self.top, width=20, font=("default", 15))
        self.entry.pack()
        self.btn = ttk.Button(self.top, text="Create", command=self.set_val)
        self.btn.pack()
        self.val = 0

    def set_val(self):
        self.val = int(self.entry.get())
        self.top.destroy()


class Grid(Tk):

    def __init__(self, screenName=None, baseName=None,
                 useTk=1, sync=0, use=None):
        super().__init__(screenName=screenName, baseName=baseName,
                         useTk=useTk, sync=sync, use=use)
        try:
            img = ImageTk.PhotoImage(Image.open(game.ENV))
        except FileNotFoundError:
            img = ImageTk.PhotoImage(Image.open(game.DEFAULT_ENV))
        # GUI
        self.title("Grid")
        self.resizable(False, False)
        self.label = ttk.Label(image=img)
        self.label.grid(row=0, column=0, columnspan=3)
        self.play_btn = ttk.Button(self, text="Play", command=self.play)
        self.play_btn.grid(row=1, column=0)
        self.play_btn["state"] = "disabled"
        self.train = ttk.Button(self, text="Train", command=self.train)
        self.train.grid(row=1, column=1)
        self.create = ttk.Button(self, text="Create env",
                                 command=self.create_env)
        self.create.grid(row=1, column=2)
        self.show = ttk.Button(self, text="Show env", command=self.show_env)
        self.show.grid(row=2, column=0)
        self.show["state"] = "disabled"
        self.table = ttk.Button(self, text="Show table",
                                command=self.show_v_table)
        self.table["state"] = "disabled"
        self.table.grid(row=2, column=1)
        self.reset = ttk.Button(self, text="Reset", command=self.reset)
        self.reset.grid(row=2, column=2)
        self.opt = ttk.Button(self, text="Optimize", command=self.optimize)
        self.opt.grid(row=3, column=0)
        self.opt["state"] = "disabled"
        self.s = BooleanVar()
        self.menubar = Menu(self)
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_checkbutton(0, label="Visual", onvalue=1,
                                 offvalue=0, variable=self.s)
        self.menubar.add_cascade(label="Tools", menu=filemenu)
        self.config(menu=self.menubar)
        self.mainloop()

    def play(self):
        try:
            TABLE = np.load("v_table.npy")
            ENVI = np.load("env.npy")
            g = play.Play(envi=ENVI, table=TABLE, size=len(TABLE))
            g.play(visual=False)
            del(g)
        except FileNotFoundError:
            pass

    def show_env(self):
        try:
            TABLE = np.load("v_table.npy")
            ENVI = np.load("env.npy")
            g = play.Play(envi=ENVI, table=TABLE, size=len(TABLE))
            g.show_env()
            del(g)
        except FileNotFoundError:
            pass
        

    def create_env(self):
        inp = Input(self)
        self.wait_window(inp.top)
        g = create.Create(size=inp.val)
        g.create_env()
        del(g, inp)
        util.Image().process(img_path=game.ENV, dim=(220, 220),
                           save=True, save_path=game.ENV)

    def train(self):
        try:
            TABLE = np.load("v_table.npy", allow_pickle=True)
            ENVI = np.load("env.npy", allow_pickle=True)
            rl = traine.Train(envi=ENVI, table=TABLE, size=len(TABLE))
            rl.train()
            del(rl)
        except FileNotFoundError:
            pass

    def show_v_table(self):
        try:
            env = np.load("env.npy")
            env_len = len(env)
            g = create.Create(size=env_len)
            # g.show_table()
            del(g)
        except FileNotFoundError:
            self.message("No such file found!")

    def reset(self):
        try:
            os.remove("v_table.npy")
        except FileNotFoundError:
            self.sound()
        try:
            os.remove("env.npy")
        except FileNotFoundError:
            self.sound()
        try:
            os.remove(game.ENV)
        except FileNotFoundError:
            self.sound()

    def optimize(self):
        o = game.Optimize()
        count = 0
        while count != len(o.action_list)-2:
            o.play()
            print(o.action_list)
            count = o.fix()
            if count == 0:
                break
            continue
        np.save("q_table", o.q_table)
        pygame.display.quit()
        del(o)

    def message(self, msg):
        messagebox.showwarning(title="Error", message=f"{msg}")

    def sound(self):
        pygame.mixer.music.load(r"C:\Windows\Media\Windows Foreground.wav")
        pygame.mixer.music.play(loops=0)


Grid()
