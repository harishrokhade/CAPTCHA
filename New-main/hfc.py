

from tkinter import *
import tkinter.messagebox
from captcha.image import ImageCaptcha
import string
import random
import os
import pyttsx3
import subprocess
import webbrowser


audio_captcha = '0'
image_captcha = ''

def close_gui():
    root.destroy()

def generate_exp_captcha():
    global expx
    expx = random.randint(6, 10)
    global expy
    expy = random.randint(1, 5)
    # expz=random.randint(1,10)
    global oper
    oper=random.randint(0,2)
    # oper1=random.randint(0,2)
    A=['+','-','*','%','//']

    exptext = "What is the value of :" + str(expx) + A[oper] + str(expy)+"   "
    Label14 = Label(RightRightFrame, font=('arial', 15, 'bold'),
                    text=exptext, padx=2, pady=2, bg="#68DEED",
                    fg="black")
    Label14.grid(row=2, column=0, sticky=W)


def check_exp_captcha():
    if oper==0:
        solu = expx + expy
    elif oper==1:
        solu = expx - expy
    elif oper==2:
        solu = expx * expy
    elif oper==3:
        solu = expx % expy
    elif oper==4:
        solu=expx//expy
    ansmid1=ansmid.get()
    print(ansmid1, solu)
    if (float(ansmid1)==(solu)):
        webbrowser.open_new("http://erp.gmit.info/axis/hostel.html")
    else:
        tkinter.messagebox.showinfo("WRONG!", "please enter the correct value")
        ansmid.set("")





def generate_captcha():
    data_set = list(string.digits)  # a-z,A-Z,0-9
    s = ''
    for i in range(4):
        a = random.choice(data_set)
        s = s + a
        data_set.remove(a)
    global image_captcha
    image_captcha = s
    return s


def generate_digit_captcha():
    s1 = ''
    s = ''
    for i in range(4):
        a = str(random.randint(0, 9))
        s = s + a
        s1 = s1 + a + " "

    global audio_captcha
    audio_captcha = s

    return s1


def generate_image_captcha():
    os.startfile('c1.png')


def generate_first_image():
    img = ImageCaptcha()

    s = generate_captcha()
    # print(s)
    value = img.generate(s)
    img.write(s, "c1.png")


def regenerate_image_captcha():
    img = ImageCaptcha()

    s = generate_captcha()
    # print(s)
    value = img.generate(s)
    img.write(s, "c1.png")
    os.startfile('c1.png')
    # print("Image Captcha Generated.\n\n")


def generate_audio_captcha():
    s = generate_digit_captcha()
    # print(s)

    voiceEngine = pyttsx3.init()

    voiceEngine.setProperty('rate', 170)
    voiceEngine.setProperty('volume', 1.0)

    voices = voiceEngine.getProperty('voices')
    voiceEngine.setProperty('voice', voices[1].id)

    voiceEngine.say(s)
    voiceEngine.runAndWait()
    voiceEngine.say(s)
    voiceEngine.runAndWait()

    # print("Audio Captcha Generated.\n\n")


def regenerate_audio_captcha():
    generate_audio_captcha()


def get_audio():
    return audio_captcha


def get_image():
    return image_captcha


def check_audio_captcha():
    # answer = input("\nEnter Value : ")
    if ans.get() == get_audio():
        # tkinter.messagebox.showinfo("SUCCESS!", "Captcha Code Matched.")
        # ans.set("")

        webbrowser.open_new("http://erp.gmit.info/axis/hostel.html")

    else:
        tkinter.messagebox.showinfo("WRONG!", "Captcha Code does not Matched.")
        ans.set("")


def check_image_captcha():
    if ans1.get() == get_image():
        # tkinter.messagebox.showinfo("SUCCESS!", "Captcha Code Matched.")
        # ans1.set("")
        webbrowser.open_new("http://erp.gmit.info/axis/hostel.html")

    else:
        tkinter.messagebox.showinfo("WRONG!", "Captcha Code does not Matched.")
        ans1.set(" ")


root = Tk()
root.title("hostel fees")

root.geometry("1200x476")

root.configure(background='white')
Tops = Frame(root, bg='#ff5c75', pady=1, width=850, height=50, relief="ridge")
Tops.grid(row=0, column=0)

ans = StringVar()
ans1 = StringVar()
ansmid =StringVar()
generate_first_image()

Title_Label = Label(Tops, font=('ALGERIAN', 20, 'bold'),
                    text="\t\t       GM INSTITUTE OF TECHNOLOGY(Hostel fees)\t\t\t", bg='skyblue',
                    fg='Beige', justify="center")
Title_Label.grid(row=0, column=0)
MainFrame = Frame(root, bg='Powder Blue',  width=1800, height=100, relief=RIDGE)
MainFrame.grid(row=1, column=0)

LeftFrame = Frame(MainFrame, bd=4, width=200, height=200, pady=2, padx=10, bg='#68DEED', relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame, bd=4, width=200, height=200, padx=2, pady=2, bg='#68DEED', relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightRightFrame=Frame(MainFrame, bd=4,  width=300, height=437, padx=2, pady=2, bg='#68DEED', relief=RIDGE)
RightRightFrame.pack(side=TOP)

Label_1 = Label(RightFrame, font=('arial', 33, 'bold'), text=" Audio Captcha ", padx=2, pady=2, bg="POWDER BLUE",
                fg="black")
Label_1.grid(row=0, column=0, sticky=W)

Label_2 = Label(RightFrame, font=('arial', 20, 'bold'), text="", padx=2, pady=2, bg="#68DEED", fg="black")
Label_2.grid(row=1, column=0, sticky=W)

Label_9 = Button(RightFrame, font=('arial', 19, 'bold'), text="Play Audio", padx=2, pady=2, bg="blue", fg="white",
                 command=generate_audio_captcha)
Label_9.grid(row=4, column=0)

Label_7 = Label(RightFrame, font=('arial', 20, 'bold'), text="", padx=2, pady=2, bg="#68DEED", fg="black")
Label_7.grid(row=2, column=0, sticky=W)

Entry_1 = Entry(RightFrame, font=('arial', 20, 'bold'), bd=2, fg="black", textvariable=ans, width=14,
                justify=LEFT).grid(row=5, column=0)

Label_7 = Label(RightFrame, font=('arial', 20, 'bold'), text="", padx=2, pady=2, bg="#68DEED", fg="black")
Label_7.grid(row=6, column=0, sticky=W)

Label_7 = Label(RightFrame, font=('arial', 20, 'bold'), text="  ", padx=2, pady=2, bg="#68DEED", fg="black")
Label_7.grid(row=6, column=1, sticky=W)

Label_8 = Button(RightFrame, font=('Arial', 25, 'bold'), text="Check", padx=2, pady=2, bg="white", fg="blue",
                 command=check_audio_captcha)
Label_8.grid(row=9, column=0)

Label_4 = Button(RightFrame, font=('arial', 15, 'bold'), text="Regenerate", padx=2, pady=2, bg="white", fg="red",
                 command=regenerate_audio_captcha)
Label_4.grid(row=10, column=0)

Label_7 = Label(RightFrame, font=('arial', 20, 'bold'), text="      ", padx=2, pady=2, bg="#68DEED", fg="black")
Label_7.grid(row=11, column=1, sticky=W)

Label_1 = Label(LeftFrame, font=('arial', 33, 'bold'), text=" Image Captcha ", padx=2, pady=2, bg="POWDER BLUE",
                fg="black")
Label_1.grid(row=0, column=0, sticky=W)

Label_2 = Label(LeftFrame, font=('arial', 20, 'bold'), text="", padx=2, pady=2, bg="#68DEED", fg="black")
Label_2.grid(row=1, column=0, sticky=W)

Label_9 = Button(LeftFrame, font=('arial', 19, 'bold'), text="Show Image", padx=2, pady=2, bg="blue", fg="white",
                 command=generate_image_captcha)
Label_9.grid(row=4, column=0)

Label_7 = Label(LeftFrame, font=('arial', 20, 'bold'), text="", padx=2, pady=2, bg="#68DEED", fg="black")
Label_7.grid(row=2, column=0, sticky=W)

Entry_1 = Entry(LeftFrame, font=('arial', 20, 'bold'), bd=2, fg="black", textvariable=ans1, width=14,
                justify=LEFT).grid(row=5, column=0)

Label_7 = Label(LeftFrame, font=('arial', 20, 'bold'), text="", padx=2, pady=2, bg="#68DEED", fg="black")
Label_7.grid(row=6, column=0, sticky=W)

Label_7 = Label(LeftFrame, font=('arial', 20, 'bold'), text="  ", padx=2, pady=2, bg="#68DEED", fg="black")
Label_7.grid(row=6, column=1, sticky=W)

Label_8 = Button(LeftFrame, font=('Arial', 25, 'bold'), text="Check", padx=2, pady=2, bg="white", fg="blue",
                 command=check_image_captcha)
Label_8.grid(row=9, column=0)

Label_4 = Button(LeftFrame, font=('arial', 15, 'bold'), text="Regenerate", padx=2, pady=2, bg="white", fg="red",
                 command=regenerate_image_captcha)
Label_4.grid(row=10, column=0)

Label_7 = Label(LeftFrame, font=('arial', 20, 'bold'), text="      ", padx=2, pady=2, bg="#68DEED", fg="black")
Label_7.grid(row=11, column=1, sticky=W)

###########################################################################
#22/07/2023

Labelnew=Label(RightRightFrame, font=('arial', 25, 'bold') , text=" Expression Captcha " , padx=2, pady=2, bg="POWDER BLUE",fg="black")
Labelnew.grid(row=0, column=0, sticky=W)
labelnew1=Label(RightRightFrame, font=('arial', 25, 'bold') , text=" " , padx=2, pady=2,bg="#68DEED", fg="black")
labelnew1.grid(row=1, column=0, sticky=W)
labelnew10=Label(RightRightFrame, font=('arial', 25, 'bold') , text=" " , padx=2, pady=2,bg="#68DEED", fg="black")
labelnew10.grid(row=3, column=0, sticky=W)
Label11 = Button(RightRightFrame, font=('arial', 19, 'bold'), text="Expression", padx=2, pady=2, bg="blue", fg="white",command=generate_exp_captcha)
Label11.grid(row=4, column=0)



Entrymid = Entry(RightRightFrame, font=('arial', 20, 'bold'), bd=2, fg="black", textvariable=ansmid, width=14,
                justify=LEFT).grid(row=7, column=0)
labelnew2=Label(RightRightFrame, font=('arial', 25, 'bold') , text=" " , padx=2, pady=2,bg="#68DEED", fg="black")
labelnew2.grid(row=8, column=0, sticky=W)
Label12 = Button(RightRightFrame, font=('Arial', 25, 'bold'), text="Check", padx=2, pady=2, bg="white", fg="blue",command=check_exp_captcha)
Label12.grid(row=11, column=0)
Label13 = Button(RightRightFrame, font=('arial', 15, 'bold'), text="Regenerate", padx=2, pady=2, bg="white", fg="red",command=generate_exp_captcha)
Label13.grid(row=12, column=0)


##############################################################################
# root.after(5000, close_gui)

root.mainloop()