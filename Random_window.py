from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.geometry("650x700")
root.config(bg="#111")
root.resizable(0, 0)
x = StringVar()
y = StringVar()
z = StringVar()
a = StringVar()
b = StringVar()
c = StringVar()

canvas = Canvas(root, width=350, height=100, bg="white")
canvas.place(x=150, y=30)
img = PhotoImage(file="img_1.png")
canvas.create_image(0, 0, anchor=NW, image=img)

# self.user_num = Entry(root, width=5,).place(x=150, y=200)
# self.user_num = Entry(root, width=5, ).place(x=200, y=200)
# self.user_num = Entry(root, width=5, ).place(x=250, y=200)
# self.user_num = Entry(root, width=5, ).place(x=300, y=200)
# self.user_num = Entry(root, width=5, ).place(x=350, y=200)
# self.user_num = Entry(root, width=5, ).place(x=400, y=200)
users_numbers = Label(root, width=17, bg="gold", textvariable=x).place(x=150, y=550)
users_numbers2 = Label(root, width=17, bg="gold", textvariable=y).place(x=150, y=580)
users_numbers3 = Label(root, width=17, bg="gold", textvariable=z).place(x=150, y=610)

Lotto_list = random.sample(range(1, 49), 6)
print(Lotto_list)

listx = []
listy = []
listz = []
match_list = []
match_list2 = []
match_list3 = []


def click(num):
    if len(listx) < 6 and num not in listx:
        listx.append(num)
        x.set(listx)

    elif len(listy) < 6 and num not in listy:
        listy.append(num)
        y.set(listy)

    elif len(listz) < 6 and num not in listz:
        listz.append(num)
        z.set(listz)


def compare():
    for num in Lotto_list:
        if num in listx:
            match_list.append(num)
            print(match_list)

    for num in Lotto_list:
        if num in listy:
            match_list2.append(num)
            print(match_list2)

    for num in Lotto_list:
        if num in listz:
            match_list3.append(num)
            print(match_list3)

    a.set("you matched " + str(len(match_list)) + " numbers")
    b.set("you matched " + str(len(match_list2)) + " numbers")
    c.set("you matched " + str(len(match_list3)) + " numbers")


match_lab1 = Label(root, bg="#111", fg="gold", textvariable=a).place(x=300, y=550)
match_lab2 = Label(root, bg="#111", fg="gold", textvariable=b).place(x=300, y=580)
match_lab3 = Label(root, bg="#111", fg="gold", textvariable=c).place(x=300, y=610)
heading = Label(root, bg="#111", text="Select 6 Lucky numbers!", fg="gold", font=20).place(x=250, y=150)

prizes = [0, 20, 100.50, 2384, 8584, 10000000]


def winnings():
    if len(match_list) < 2:
        a.set("You won R" + str(prizes[0]))
    elif len(match_list) == 2:
        a.set("You won R" + str(prizes[1]))
    elif len(match_list) == 3:
        a.set("You won R" + str(prizes[2]))
    elif len(match_list) == 4:
        a.set("You won R" + str(prizes[3]))
    elif len(match_list) == 5:
        a.set("You won R" + str(prizes[4]))
    elif len(match_list) == 6:
        a.set("You won R" + str(prizes[5]))

    if len(match_list2) < 2:
        b.set("You won R" + str(prizes[0]))
    elif len(match_list2) == 2:
        b.set("You won R" + str(prizes[1]))
    elif len(match_list2) == 3:
        b.set("You won R" + str(prizes[2]))
    elif len(match_list2) == 4:
        b.set("You won R" + str(prizes[3]))
    elif len(match_list2) == 5:
        b.set("You won R" + str(prizes[4]))
    elif len(match_list2) == 6:
        b.set("You won R" + str(prizes[5]))

    if len(match_list3) < 2:
        c.set("You won R" + str(prizes[0]))
    elif len(match_list3) == 2:
        c.set("You won R" + str(prizes[1]))
    elif len(match_list3) == 3:
        c.set("You won R" + str(prizes[2]))
    elif len(match_list3) == 4:
        c.set("You won R" + str(prizes[3]))
    elif len(match_list3) == 5:
        c.set("You won R" + str(prizes[4]))
    elif len(match_list3) == 6:
        c.set("You won R" + str(prizes[5]))


total_wins_btn = Button(root, text="total").place(x=400, y=650)
winnings_btn = Button(root, text="Winnings", command=winnings).place(x=300, y=650)
play_btn = Button(root, text="Play", bg="gold", command=compare, width=14).place(x=150, y=650)
num_select1 = Button(root, width=2, bg="gold", text="1", command=lambda: click(1)).place(x=150, y=200)
num_select2 = Button(root, width=2, bg="gold", text="2", command=lambda: click(2)).place(x=200, y=200)
num_select3 = Button(root, width=2, bg="gold", text="3", command=lambda: click(3)).place(x=250, y=200)
num_select4 = Button(root, width=2, bg="gold", text="4", command=lambda: click(4)).place(x=300, y=200)
num_select5 = Button(root, width=2, bg="gold", text="5", command=lambda: click(5)).place(x=350, y=200)
num_select7 = Button(root, width=2, bg="gold", text="6", command=lambda: click(6)).place(x=400, y=200)
num_select8 = Button(root, width=2, bg="gold", text="7", command=lambda: click(7)).place(x=450, y=200)
num_select9 = Button(root, width=2, bg="gold", text="8", command=lambda: click(8)).place(x=150, y=250)
num_select10 = Button(root, width=2, bg="gold", text="9", command=lambda: click(9)).place(x=200, y=250)
num_select11 = Button(root, width=2, bg="gold", text="10", command=lambda: click(10)).place(x=250, y=250)
num_select12 = Button(root, width=2, bg="gold", text="11", command=lambda: click(11)).place(x=300, y=250)
num_select13 = Button(root, width=2, bg="gold", text="12", command=lambda: click(12)).place(x=350, y=250)
num_select14 = Button(root, width=2, bg="gold", text="13", command=lambda: click(13)).place(x=400, y=250)
num_select15 = Button(root, width=2, bg="gold", text="14", command=lambda: click(14)).place(x=450, y=250)
num_select16 = Button(root, width=2, bg="gold", text="15", command=lambda: click(15)).place(x=150, y=300)
num_select17 = Button(root, width=2, bg="gold", text="16", command=lambda: click(16)).place(x=200, y=300)
num_select18 = Button(root, width=2, bg="gold", text="17", command=lambda: click(17)).place(x=250, y=300)
num_select19 = Button(root, width=2, bg="gold", text="18", command=lambda: click(18)).place(x=300, y=300)
num_select20 = Button(root, width=2, bg="gold", text="19", command=lambda: click(19)).place(x=350, y=300)
num_select21 = Button(root, width=2, bg="gold", text="20", command=lambda: click(20)).place(x=400, y=300)
num_select22 = Button(root, width=2, bg="gold", text="21", command=lambda: click(21)).place(x=450, y=300)
num_select23 = Button(root, width=2, bg="gold", text="22", command=lambda: click(22)).place(x=150, y=350)
num_select24 = Button(root, width=2, bg="gold", text="23", command=lambda: click(23)).place(x=200, y=350)
num_select25 = Button(root, width=2, bg="gold", text="24", command=lambda: click(24)).place(x=250, y=350)
num_select26 = Button(root, width=2, bg="gold", text="25", command=lambda: click(25)).place(x=300, y=350)
num_select27 = Button(root, width=2, bg="gold", text="26", command=lambda: click(26)).place(x=350, y=350)
num_select28 = Button(root, width=2, bg="gold", text="27", command=lambda: click(27)).place(x=400, y=350)
num_select29 = Button(root, width=2, bg="gold", text="28", command=lambda: click(28)).place(x=450, y=350)
num_select30 = Button(root, width=2, bg="gold", text="29", command=lambda: click(29)).place(x=150, y=400)
num_select31 = Button(root, width=2, bg="gold", text="30", command=lambda: click(30)).place(x=200, y=400)
num_select32 = Button(root, width=2, bg="gold", text="31", command=lambda: click(31)).place(x=250, y=400)
num_select33 = Button(root, width=2, bg="gold", text="32", command=lambda: click(32)).place(x=300, y=400)
num_select34 = Button(root, width=2, bg="gold", text="33", command=lambda: click(33)).place(x=350, y=400)
num_select35 = Button(root, width=2, bg="gold", text="34", command=lambda: click(34)).place(x=400, y=400)
num_select36 = Button(root, width=2, bg="gold", text="35", command=lambda: click(35)).place(x=450, y=400)
num_select37 = Button(root, width=2, bg="gold", text="36", command=lambda: click(36)).place(x=150, y=450)
num_select38 = Button(root, width=2, bg="gold", text="37", command=lambda: click(37)).place(x=200, y=450)
num_select39 = Button(root, width=2, bg="gold", text="38", command=lambda: click(38)).place(x=250, y=450)
num_select40 = Button(root, width=2, bg="gold", text="39", command=lambda: click(39)).place(x=300, y=450)
num_select41 = Button(root, width=2, bg="gold", text="40", command=lambda: click(40)).place(x=350, y=450)
num_select42 = Button(root, width=2, bg="gold", text="41", command=lambda: click(41)).place(x=400, y=450)
num_select43 = Button(root, width=2, bg="gold", text="42", command=lambda: click(42)).place(x=450, y=450)
num_select44 = Button(root, width=2, bg="gold", text="43", command=lambda: click(43)).place(x=150, y=500)
num_select45 = Button(root, width=2, bg="gold", text="44", command=lambda: click(44)).place(x=200, y=500)
num_select46 = Button(root, width=2, bg="gold", text="45", command=lambda: click(45)).place(x=250, y=500)
num_select47 = Button(root, width=2, bg="gold", text="46", command=lambda: click(46)).place(x=300, y=500)
num_select48 = Button(root, width=2, bg="gold", text="47", command=lambda: click(47)).place(x=350, y=500)
num_select49 = Button(root, width=2, bg="gold", text="48", command=lambda: click(48)).place(x=400, y=500)
num_select50 = Button(root, width=2, bg="gold", text="49", command=lambda: click(49)).place(x=450, y=500)

root.mainloop()
