from datetime import datetime
import subprocess
import os

PATH_PASS = r"C:/ProgramData/Simple Note/PIN.txt"
PATH_NOTE = r"C:/ProgramData/Simple Note/test.txt"
PATH_FIRST = r"C:/ProgramData/Simple Note/a Simple note.txt"
FILE_DIR = r"C:/ProgramData/Simple Note"


def clear():
    os.system('cls')


def first():
    try:
        os.makedirs(FILE_DIR)
    except FileExistsError:
        pass
    note = open(os.path.expanduser(PATH_FIRST), "w+")
    note.write(
        """<<<<<<<<<<<<<<<<<<<<<<<< SIMPLE NOTE >>>>>>>>>>>>>>>>>>>>>>>>>>
                            Simple Note - ver(2.0)
                            Python - ver(3.8)
                            Lightnings's Theme - Radiance
                                 © 2020 GANTULGA
    """)
    fido = open(os.path.expanduser(PATH_PASS), "w+")
    open(os.path.expanduser(PATH_NOTE), "w+")
    while True:
        pin1 = int(input("Create PIN : "))
        clear()
        pin1i = int(input("Enter PIN again :"))
        if pin1i == pin1:
            break
        else:
            print("Wrong entry")
    fido.write(str(pin1))
    subprocess.check_call(["attrib", "+H", PATH_PASS])
    subprocess.check_call(["attrib", "+H", PATH_NOTE])
    fido.close()
    return pin1


def _input(pin1):
    y = 0
    while y < 5:
        inp = input("Enter PIN : ")
        clear()
        if inp.isdigit() is True:
            inp = int(inp)
            if inp == pin1:
                return True
            else:
                y += 1
                print("Wrong number ")
        else:
            print("Wrong input!!!")
    print("You've entered wrong PIN 5 times >>> Your note file will be deleted")
    return False


def restart():
    if os.path.exists(PATH_NOTE):
        os.remove(PATH_NOTE)
        os.remove(PATH_PASS)
        os.remove(PATH_FIRST)
    else:
        print("The file does not exist")


class FileAccess:

    def __init__(self):
        fid1 = open(os.path.expanduser(PATH_NOTE), "r")
        self.note = fid1.read()
        print(self.note)
        fid1.close()

    @staticmethod
    def write(note):
        now = datetime.now()
        with open(os.path.expanduser(PATH_NOTE), "a") as fid1:
            fid1.write(now.strftime("%D - %H:%M:%S") + "\n" + note + "\n\n")

    @staticmethod
    def clear1():
        os.remove(PATH_NOTE)
        open(os.path.expanduser(PATH_NOTE), "wt")


try:
    fid = open(PATH_PASS, "r")
    try:
        pin = int(fid.read())
        fid.close()
    except ValueError:
        fid.close()
        restart()
        pin = first()
except FileNotFoundError as Error:
    pin = first()
if _input(pin):
    while True:
        clear()
        x = FileAccess()
        b = input("Note : ")
        if b == "CLEAR":
            x.clear1()
        elif b == "CLOSE":
            break
        else:
            x.write(b)
else:
    restart()
    input("Press any key to EXIT>>>")
