from tkinter import *
from tkinter import font as tkFont 
import sys
import os

root = Tk()
root.title("Canvasky GUI")

myMenu = Menu()
root.config(menu=myMenu)
myMenu.add_cascade(label="Main Menu")
myMenu.add_cascade(label="Instruction")
myMenu.add_cascade(label="More Settings")
ExitFont = tkFont.Font(family='Helvetica', size=20, weight='bold')
NormalFont = tkFont.Font(family='Helvetica', size=20, weight='bold')
TitleFont = tkFont.Font(family='Calibri', size=80)

#text on screen
MyLabel = Label(text="Canvasky",fg="#FCF3CF",bg='#F5B7B1',font=TitleFont).place(x=170,y=100)

#test chuey2 ja
def showMessage():
    Label(text="Welcome to Canvasky !",fg="pink",font=100).place(x=0,y=450)

def hidebtn():
    btn4.place_forget()

def showbtn():
    btn4.place(x=500,y=380)

def init_canvas():
    os.system('python handtracking.py')
    root.destroy()


#button variables
btn1 = Button(root,text="Begin",fg='#97DDE5',font=NormalFont,command=init_canvas)
btn2= Button(root,text="Exit",bg='red',fg='#CD6155',font=ExitFont,command=root.destroy)
btn3= Button(root,text="Instruction",fg='#C39BD3',font=NormalFont,command=hidebtn)
btn4= Button(root,text="Setting",fg="#82E0AA",font=NormalFont)

def place_menu():
    btn1.place(x=120,y=280)
    btn3.place(x=470,y=280) 
    btn4.place(x=115,y=380)
    btn2.place(x=500,y=380)

place_menu()


# size and pos of monitor
root.geometry("700x550+450+200")
root.configure(bg='#F5B7B1')
root.mainloop()
