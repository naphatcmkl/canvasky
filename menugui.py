from tkinter import *
from tkinter import font as tkFont 
import sys
import os

root = Tk()
root.title("Canvasky")

myMenu = Menu()
root.config(menu=myMenu)
# myMenu.add_cascade(label="Main Menu")
# myMenu.add_cascade(label="Instruction")
# myMenu.add_cascade(label="More Settings")
ExitFont = tkFont.Font(family='Helvetica', size=20, weight='bold')
NormalFont = tkFont.Font(family='Helvetica', size=20, weight='bold')
TitleFont = tkFont.Font(family='Calibri', size=80)
statusFont = tkFont.Font(family='Calibri', size=20)

# setting_opts = open("setting.txt", "r")
# print("setting: ", setting_opts.read())
# setting_file = setting_opts.read()
# setting = []
# for each in setting_file:
#     print(each)
#     setting.append(each)
# print("setting array: ",setting)



#text on screen
MyLabel = Label(text="Canvasky",fg="#FCF3CF",bg='#F5B7B1',font=TitleFont)
status = StringVar()

#test chuey2 ja
def showMessage():
    Label(text="Creating your canvas, Please wait a moment...",fg="pink",font=100).place(x=0,y=450)

def hidebtn():
    btn4.place_forget()

def showbtn():
    btn4.place(x=500,y=450)

def init_canvas():
    status.set("Creating your canvas, please wait a moment...")
    os.system('python handtracking.py')
    root.destroy()

def setting_click():
    forget_all_menu()
    place_setting()

def back_click():
    forget_all_setting()
    clear_brushset()
    place_menu()
    






def place_menu():
    btn1.place(x=170,y=280)
    btn3.place(x=510,y=280) 
    btn4.place(x=170,y=380)
    btn2.place(x=510,y=380)
    status.set("hello")
    status_text.place(x=170,y=450)
    MyLabel.place(x=220,y=100)

def forget_all_menu():
    MyLabel.place_forget()
    btn1.place_forget()
    btn2.place_forget()
    btn3.place_forget()
    btn4.place_forget()
    status_text.place_forget()

def default_brush():
    print("changing back to default...")
    clear_brushset()

    default_setting = []
    default_thickness =  ['5', '10', '20', '40', '60', '80', '60']
    setting_all = get_setting()
    all_other = setting_all[7:]
    default_setting += default_thickness + all_other
    file_writer = open("setting.txt","w")
    for j in range(len(default_setting)):
        file_writer.write(default_setting[j]+"\n")
    file_writer.close()

    setting_checker(0)
    print("default set !")

def cmd_checker(cmd):
    cmd = str(cmd)
    failed = False

    return failed

def rgb_checker(r,g,b):
    r = str(r)
    g = str(g)
    b = str(b)

    failed = False
    return failed


def color_adder():
    cmdGet = str(commEn.get())
    rGet = str(redEn.get())
    gGet = str(grnEn.get())
    bGet = str(bluEn.get())
    cmd_checked = cmd_checker(cmdGet)
    rgb_checked = rgb_checker(rGet,gGet,bGet)
    if cmd_checked and rgb_checked:
        print("adding color..")

        print("color added")
    else:
        print("error adding color")


def int_checker(num):
    num = str(num)
    if num[0] in ('-','+'):
        return num[1:].isdigit()
    else:
        return num.isdigit()


def save_brush():
    tinyGet = str(tinyEn.get())
    smallGet = str(smallEn.get())
    mediumGet = str(mediumEn.get())
    bigGet = str(bigEn.get())
    hugeGet = str(hugeEn.get())
    giantGet = str(giantEn.get())
    eraseGet = str(erthickEn.get())
    failed = False
    if tinyGet == "":
        tinyGet = str(tinyVar.get())
    if smallGet == "":
        smallGet = str(smallVar.get())
    if mediumGet == "":
        mediumGet = str(mediumVar.get())
    if bigGet == "":
        bigGet = str(bigVar.get())
    if hugeGet == "":
        hugeGet = str(hugeVar.get())
    if giantGet == "":
        giantGet = str(giantVar.get())
    if eraseGet == "":
        eraseGet = str(erthickVar.get())
    if not tinyGet.isdigit():
        print(tinyGet)
        tinyEn.delete(0, END)
        failed = True
    if not smallGet.isdigit():
        print(smallGet)
        smallEn.delete(0, END)
        failed = True
    if not mediumGet.isdigit():
        print(mediumGet)
        mediumEn.delete(0, END)
        failed = True
    if not bigGet.isdigit():
        print(bigGet)
        bigEn.delete(0, END)
        failed = True
    if not hugeGet.isdigit():
        print(hugeGet)
        hugeEn.delete(0, END)
        failed = True
    if not giantGet.isdigit():
        print(giantGet)
        giantEn.delete(0, END)
        failed = True
    if not eraseGet.isdigit():
        print(eraseGet)
        erthickEn.delete(0, END)
        failed = True
    if not failed:
        print("saving..")
        clear_brushset()

        new_setting = []
        setting_all = get_setting()
        all_other = setting_all[7:]
        new_setting.append(tinyGet)
        new_setting.append(smallGet)
        new_setting.append(mediumGet)
        new_setting.append(bigGet)
        new_setting.append(hugeGet)
        new_setting.append(giantGet)
        new_setting.append(eraseGet)
        new_setting += all_other

        file_writer = open("setting.txt","w")
        for j in range(len(new_setting)):
            file_writer.write(new_setting[j]+"\n")
        file_writer.close()

        setting_checker(0)
        print("save changed")
    else:
        print("error type")

    

def clear_brushset():
    tinyEn.delete(0, END)
    smallEn.delete(0, END)
    mediumEn.delete(0, END)
    bigEn.delete(0, END)
    hugeEn.delete(0, END)
    giantEn.delete(0, END)
    erthickEn.delete(0, END)

def get_setting():
    setting_file = open("setting.txt","r")
    all_setting = setting_file.read().splitlines()
    return all_setting

def color_set(color_list):
    for i in range (len(color_list)):
        box.insert(END, color_list[i])

def setting_checker(many):
    setting_all = get_setting()
    all_other = setting_all[7:]
    tiny_th = setting_all[0]
    small_th = setting_all[1]
    medium_th = setting_all[2]
    big_th = setting_all[3]
    huge_th = setting_all[4]
    giant_th = setting_all[5]
    eraser_thick = setting_all[6]
    tinyVar.set(str(tiny_th))
    smallVar.set(str(small_th))
    mediumVar.set(str(medium_th))
    bigVar.set(str(big_th))
    hugeVar.set(str(huge_th))
    giantVar.set(str(giant_th))
    erthickVar.set(str(eraser_thick))
    print("all setting: ", setting_all ," color setting: ",all_other)
    next_color = 0
    other_color = []
    other_rgb = []
    for i in range (len(all_other)):
        if i == next_color:
            other_color.append(all_other[i])
            next_color += 4
        else:
            other_rgb.append(all_other[i])
    if many == 1:
        color_set(other_color)

#button variables
btn1 = Button(root, text="Begin", fg='#97DDE5', height=2, width=10, font=NormalFont, command=init_canvas)
btn2= Button(root,text="Exit", fg='#CD6155', height=2, width=10, font=ExitFont, command=root.destroy)
btn3= Button(root,text="Instruction", fg='#C39BD3', height=2, width=10, font=NormalFont, command=hidebtn)
btn4= Button(root,text="Setting", fg="#82E0AA", height=2, width=10, font=NormalFont, command=setting_click)
status_text = Label(textvariable=status, bg='#F5B7B1', fg="white", font=statusFont)

#status variable
setting = Label(root, text="Setting", bg='#F5B7B1', fg="white",  font=('Thonburi 22 bold'))
brthick = Label(root, text="Brush thickness", bg='#F5B7B1', fg="white",  font=('Thonburi 20 bold'))
tiny = Label(root, text="tiny", bg='#F5B7B1', fg="white",  font=('Thonburi', 20))
tinyVar = StringVar()
tinyV = Label(textvariable=tinyVar, bg='#F5B7B1', fg="white", font=('Thonburi', 18))
tinyEn = Entry(root)
small = Label(root, text="small", bg='#F5B7B1', fg="white",  font=('Thonburi', 20))
smallVar = StringVar()
smallV = Label(textvariable=smallVar, bg='#F5B7B1', fg="white", font=('Thonburi', 18))
smallEn = Entry(root)
medium = Label(root, text="medium", bg='#F5B7B1', fg="white",  font=('Thonburi', 20))
mediumVar = StringVar()
mediumV = Label(textvariable=mediumVar, bg='#F5B7B1', fg="white", font=('Thonburi', 18))
mediumEn = Entry(root)
big = Label(root, text="big", bg='#F5B7B1', fg="white",  font=('Thonburi', 20))
bigVar = StringVar()
bigV = Label(textvariable=bigVar, bg='#F5B7B1', fg="white", font=('Thonburi', 18))
bigEn = Entry(root)
huge = Label(root, text="huge", bg='#F5B7B1', fg="white",  font=('Thonburi', 20))
hugeVar = StringVar()
hugeV = Label(textvariable=hugeVar, bg='#F5B7B1', fg="white", font=('Thonburi', 18))
hugeEn = Entry(root)
giant = Label(root, text="giant", bg='#F5B7B1', fg="white",  font=('Thonburi', 20))
giantVar = StringVar()
giantV = Label(textvariable=giantVar, bg='#F5B7B1', fg="white", font=('Thonburi', 18))
giantEn = Entry(root)
erthick = Label(root, text="eraser thickness", bg='#F5B7B1', fg="white",  font=('Thonburi', 20))
erthickVar = StringVar()
erthickV = Label(textvariable=erthickVar, bg='#F5B7B1', fg="white", font=('Thonburi', 18))
erthickEn = Entry(root)
to1 = Label(root, text="to", bg='#F5B7B1', fg="white", font=('Thonburi', 20))
to2 = Label(root, text="to", bg='#F5B7B1', fg="white",  font=('Thonburi', 20))
to3 = Label(root, text="to", bg='#F5B7B1', fg="white",  font=('Thonburi', 20))
to4 = Label(root, text="to", bg='#F5B7B1', fg="white",  font=('Thonburi', 20))
to5 = Label(root, text="to", bg='#F5B7B1', fg="white",  font=('Thonburi', 20))
to6 = Label(root, text="to", bg='#F5B7B1', fg="white",  font=('Thonburi', 20))
to7 = Label(root, text="to", bg='#F5B7B1', fg="white",  font=('Thonburi', 20))
color = Label(root, text="More color", bg='#F5B7B1', fg="white",  font=('Thonburi 22 bold'))
comm = Label(root, text="command", bg='#F5B7B1', fg="white",  font=('Thonburi', 20))
commEn = Entry(root)
red = Label(root, text="R", bg='#F5B7B1', fg="white",  font=('Thonburi 18 bold'))
redEn = Entry(root)
grn = Label(root, text="G", bg='#F5B7B1', fg="white",  font=('Thonburi 18 bold'))
grnEn = Entry(root)
blu = Label(root, text="B", bg='#F5B7B1', fg="white",  font=('Thonburi 18 bold'))
bluEn = Entry(root)
save = Button(root, text="SAVE", fg='#97DDE5', width=10, font=('Thonburi 20 bold'),command= save_brush)
default = Button(root, text="DEFAULT", fg='#CD6155', width=10, font=('Thonburi 20 bold'),command= default_brush)
back= Button(root, text="BACK", fg='#82E0AA', width=10, font=('Thonburi 20 bold'), command=back_click)
box = Listbox(root, bg="#fffde7", fg="black", borderwidth=0, highlightthickness=0, font=('Thonburi', 20), height=7, width=18)
add = Button(root, text="ADD", fg='#97DDE5', width=10, font=('Thonburi 20 bold'))
delete = Button(root, text="DELETE", fg='#CD6155', width=10, font=('Thonburi 20 bold'))


def place_setting():
    setting.place(x=20, y=20)
    brthick.place(x=40, y=60)
    tiny.place(x=50, y=90)
    tinyVar.set("555")
    tinyV.place(x=110, y=92)
    to1.place(x=140, y=90)
    tinyEn.place(x=180, y=96, height=25, width=50)
    small.place(x=50, y=120)
    smallVar.set("10")
    smallV.place(x=110, y=122)
    to2.place(x=140, y=120)
    smallEn.place(x=180, y=126, height=25, width=50)
    medium.place(x=260, y=90)
    mediumVar.set("20")
    mediumV.place(x=350, y=92)
    to3.place(x=380, y=90)
    mediumEn.place(x=420, y=96, height=25, width=50)
    big.place(x=260, y=120)
    bigVar.set("40")
    bigV.place(x=350, y=122)
    to4.place(x=380, y=120)
    bigEn.place(x=420, y=126, height=25, width=50)
    huge.place(x=500, y=90)
    hugeVar.set("60")
    hugeV.place(x=570, y=92)
    to5.place(x=600, y=90)
    hugeEn.place(x=640, y=96, height=25, width=50)
    giant.place(x=500, y=120)
    giantVar.set("80")
    giantV.place(x=570, y=122)
    to6.place(x=600, y=120)
    giantEn.place(x=640, y=126, height=25, width=50)
    erthick.place(x=50, y=165)
    erthickVar.set("60")
    erthickV.place(x=230, y=167)
    to7.place(x=260, y=165)
    erthickEn.place(x=300, y=169, height=25, width=50)
    back.place(x=620, y=24)
    save.place(x=180, y=210)
    default.place(x=420, y=210)
    color.place(x=20, y=260)
    box.place(x=60, y=315)
    comm.place(x=350, y=315)
    commEn.place(x=480, y=317, height=30, width=150)
    red.place(x=350, y=360)
    redEn.place(x=380, y=362, height=30, width=70)
    grn.place(x=470, y=360)
    grnEn.place(x=500, y=362, height=30, width=70)
    blu.place(x=590, y=360)
    bluEn.place(x=620, y=362, height=30, width=70)
    add.place(x=370, y=440)
    delete.place(x=540, y=440)
    setting_checker(1)

def forget_all_setting():
    setting.place_forget()
    brthick.place_forget()
    tiny.place_forget()
    tinyV.place_forget()
    tinyEn.place_forget()
    small.place_forget()
    smallV.place_forget()
    smallEn.place_forget()
    medium.place_forget()
    mediumV.place_forget()
    mediumEn.place_forget()
    big.place_forget()
    bigV.place_forget()
    bigEn.place_forget()
    huge.place_forget()
    hugeV.place_forget()
    hugeEn.place_forget()
    giant.place_forget()
    giantV.place_forget()
    giantEn.place_forget()
    erthick.place_forget()
    erthickV.place_forget()
    erthickEn.place_forget()
    to1.place_forget()
    to2.place_forget()
    to3.place_forget()
    to4.place_forget()
    to5.place_forget()
    to6.place_forget()
    to7.place_forget()
    save.place_forget()
    default.place_forget()
    color.place_forget()
    box.place_forget()
    comm.place_forget()
    commEn.place_forget()
    red.place_forget()
    redEn.place_forget()
    grn.place_forget()
    grnEn.place_forget()
    blu.place_forget()
    bluEn.place_forget()
    add.place_forget()
    delete.place_forget()
    back.place_forget()

place_menu()
print(tkFont.families())
print(tkFont.names())


# size and pos of monitor
root.geometry("800x550+400+150")
root.configure(bg='#F5B7B1')
root.mainloop()