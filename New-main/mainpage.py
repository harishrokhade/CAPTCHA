from tkinter import*

import subprocess
import webbrowser


gui=Tk()
gui.geometry("1920x1080")
gui.title("first page")
gui.config(background="skyblue")
lbl=Label(gui,text="GM INSTITUTE OF TECHNOLOGY",font=("times new roman",40),background="skyblue",fg="Beige")
lbl.place(x=130,y=10)
lbl2=Label(gui, text="Department of Computer science and Engineering", font=("times new roman",25), background="skyblue")
lbl2.place(x=135,y=65)
lbl3=Label(gui,text="-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",font=("times new roman",15),fg="#a4a199", background="skyblue")

lbl3.place(x=0,y=110)
lbl8=Label(gui,text="-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",font=("times new roman",15),fg="#a4a199", background="skyblue")
lbl8.place(x=0,y=160)

lbl4=Label(gui,text="FEES PORTAL PROTECTION FROM BOT USING AUDIO CAPTCHA AND IMAGE CAPTCHA",font=("algerian",22),fg="darkblue",background="skyblue")
lbl4.place(x=20,y=130)
def runcode():
    cmd='python second.py'
    p=subprocess.Popen(cmd,shell=True)
projectbutton = Button(gui,text="Fees Payment" ,bg="red",fg="white", command=runcode,font=('times new roman',20))
projectbutton.place(x=950,y=250)

lbl80=Label(gui,text="Our Team : ",font=("times new roman",25),fg="black",background="skyblue")
lbl80.place(x=20,y=200)


logoimg=PhotoImage(file="Logogmit.png")
logobutton=Label(gui,image=logoimg)
logobutton.place(x=0,y=0)

def harish():
    # webbrowser.open_new("harish.pdf")
    webbrowser.open_new("https://www.linkedin.com/in/harish-r-672276229?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3B0NGOfLiFSkmotol6LRYZ%2BA%3D%3D")
harishimg = PhotoImage(file="harish.png")
harishbutton = Button(gui, image=harishimg, bg="skyblue", command=harish)
harishbutton.place(x=40, y=250)
hrn=Label(gui,text="HARISH R ROKHADE\n4GM21CS038",font=("times new roman",10),bg="skyblue",fg="black")
hrn.place(x=40,y=450)

def ananya():
    webbrowser.open_new("ananya.pdf")
ananyaimg = PhotoImage(file="Ananya N G.png")
ananyabutton = Button(gui, image=ananyaimg ,bg="skyblue", command=ananya)
ananyabutton.place(x=210, y=250)
an=Label(gui,text="ANANYA N G\n4GM21CS009",font=("times new roman",15),bg="skyblue",fg="black")
an.place(x=210,y=445)

def adithya():
    webbrowser.open_new("www.linkedin.com/in/AvGeek")
    # webbrowser.open_new("adithya.pdf")
adithyaimg = PhotoImage(file="Adithya.png")
adithyabutton = Button(gui, image=adithyaimg ,bg="skyblue", command=adithya)
adithyabutton.place(x=380, y=250)
abmn=Label(gui,text="ADITHYA B M\n4GM21CS006",font=("times new roman",15),bg="skyblue",fg="black")
abmn.place(x=380,y=445)


def aishwarya():
    webbrowser.open_new("aish.pdf")
aishwaryaimg = PhotoImage(file="aish.png")
aishwaryabutton = Button(gui, image=aishwaryaimg ,bg="skyblue", command=aishwarya)
aishwaryabutton.place(x=550, y=250)
ansn=Label(gui,text="AISHWARYA N SURVE\n4GM21CS007",font=("times new roman",10),bg="skyblue",fg="black")
ansn.place(x=550,y=445)

lbl5=Label(gui,text="Our Project: ",font=("times new roman",25),bg="skyblue")
lbl5.place(x=800,y=200)

lbl6=Label(gui,text="Project Report:",font=("times new roman",25),bg="skyblue")
lbl6.place(x=800,y=340)

def report():
    webbrowser.open_new("captcha report.pdf")
reportbutton = Button(gui, text="Report", bg="red",fg="white", font=("times new roman",20),command=report)
reportbutton.place(x=950,y=390)

avgeek=Label(gui,text="End to End development by AvGeek",font=("times new roman",8),bg="skyblue",fg="black")
avgeek.place(x=1100,y=630)

guide=Label(gui,text="Project Guided by: ",font=("Montserrat",25),fg="black",bg="skyblue")
guide.place(x=20,y=510)

guidename=Label(gui,text="Prof.Kotreshi S N ",font=("Russo One",20),fg="black",bg="skyblue")
guidename.place(x=90,y=550)


gui.mainloop()
