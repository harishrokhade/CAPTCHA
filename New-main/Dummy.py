import webbrowser
from tkinter import *
from PIL import ImageTk
import subprocess

gui = Tk()
gui.geometry("1920x1080")
gui.title("2nd Page")

logoimg=PhotoImage(file="C:/Users/HP/Desktop/AAMMU.HTML/My documents/Myproject1.png")
logobutton=Label(gui,image=logoimg)
logobutton.place(x=0,y=0)

# image_0=Image.open("C:/Users/HP/Desktop/images/siting.png")
# bgr=ImageTk.PhotoImage(image_0)
# lbl1=Label(gui,image=bgr).place(x=0,y=0)

gui.configure(background="white")

# lbl=Label(gui,text="GMIT ERP LOGIN",font=("calibri,25"),bg="white").place(x=50,y=105)
def clgfees():
    cmd = 'python cfc.py'
    p =subprocess.Popen(cmd, shell=True)
abtimg=Button(gui,text="\t\t   COLLEGE FEES\t\t\t",font=("times new roman",20),fg="white",bg="purple",command=clgfees)
abtimg.place(x=300,y=80)

# lbl_2=Label(gui,text="HACKATHON",font=("calibri,25"),bg="white").place(x=50,y=150)
def hostelfees():
    cmd = 'python hfc.py'
    p = subprocess.Popen(cmd, shell=True)


abtimg = Button(gui, text="\t\t    HOSTEL FEES\t\t\t", font=("times new roman", 20), fg="white", bg="purple", command=hostelfees)
abtimg.place(x=300, y=160)


# lbl_3=Label(gui,text="W3SCHOOLS",font=("calibri,25"),bg="white").place(x=50,y=195)
def examfees():
    cmd = 'python efc.py'
    p = subprocess.Popen(cmd, shell=True)


abtimg = Button(gui, text="\t      EXAM/RE EVALUATION FEES\t\t", font=("times new roman", 20), fg="white", bg="purple",
                command=examfees)
abtimg.place(x=300, y=240)


def recipt():
    cmd = 'python drc.py'
    p = subprocess.Popen(cmd, shell=True)


abtimg = Button(gui, text="\t\tDOWNLOAD RECIPTS\t\t", font=("times new roman", 20), fg="white", bg="green",
                command=recipt)
abtimg.place(x=300, y=320)


def paygre():
    cmd = 'python pyc.py'
    p = subprocess.Popen(cmd, shell=True)


abtimg = Button(gui, text="\t\tPAYMENT GRIEVANCE\t\t", font=("times new roman", 20), fg="white", bg="red",
                command=paygre)
abtimg.place(x=300, y=400)
def greres():
    cmd = 'python greres.py'
    p = subprocess.Popen(cmd, shell=True)


abtimg = Button(gui, text="\t\tGRIEVANCE RESULT\t\t", font=("times new roman", 20), fg="white", bg="red",
                command=greres)
abtimg.place(x=300, y=480)
def book():
    cmd = 'python booking.py'
    p = subprocess.Popen(cmd, shell=True)


abtimg = Button(gui, text="booking", font=("times new roman", 8), fg="blue", bg="grey",
                command=book)
abtimg.place(x=300, y=560)

gui.mainloop()