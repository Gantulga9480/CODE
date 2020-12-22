from tkinter import *
from PIL import ImageTk, Image


def forward(img_num):
    label = Label(image=img)
    label.grid(row=0, column=0, columnspan=3)

    btn_back = Button(root, text="<<", command=back)
    btn_exit = Button(root, text="exit", command=root.quit)
    btn_forward = Button(root, text=">>", command=lambda: forward(2))

    btn_back.grid(row=1, column=0)
    btn_exit.grid(row=1, column=1)
    btn_forward.grid(row=1, column=2)


def back():
    pass


root = Tk()
root.title("Image GUI")
# root.iconbitmap("D:/Coding Folder/PYTHON/GameCourse/Sudoku/game.ico")

img = ImageTk.PhotoImage(Image.open("image.jpg"))
img1 = ImageTk.PhotoImage(Image.open("img1.jpg"))
img2 = ImageTk.PhotoImage(Image.open("img2.jpg"))
img_list = [img, img1, img2]

label = Label(image=img)
label.grid(row=0, column=0, columnspan=3)

btn_back = Button(root, text="<<", command=back)
btn_exit = Button(root, text="exit", command=root.quit)
btn_forward = Button(root, text=">>", command=lambda: forward(2))

btn_back.grid(row=1, column=0)
btn_exit.grid(row=1, column=1)
btn_forward.grid(row=1, column=2)

root.mainloop()
