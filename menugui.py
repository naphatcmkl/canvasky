from tkinter import *
from tkinter import font as tkFont 

root = Tk()
root.title("Canvasky GUI")
#helv36 = tkFont.Font(family='Helvetica', size=36, weight='bold')

myMenu = Menu()
root.config(menu=myMenu)
myMenu.add_cascade(label="Main Menu")
myMenu.add_cascade(label="Instruction")
myMenu.add_cascade(label="More Settings")

#text on screen
MyLabel = Label(text="Canvasky",fg="green",font=("Helvetica",100)).place(x=260,y=100)
#MyLabel['font'] = helv36

#test chuey2 ja
def showMessage():
    Label(text="Welcome to Canvasky !",fg="pink",font=100).place(x=0,y=400)

#button
btn1 = Button(text="Begin",fg="black",command=showMessage).place(x=120,y=200)
btn2= Button(text="Exit",bg="green").place(x=420,y=200)

# size and pos of monitor
root.geometry("600x500+450+200")
root.mainloop()
