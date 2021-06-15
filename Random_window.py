from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.geometry("650x600")
root.config(bg="#111")


class Play:
    def __init__(self):
        self.canvas = Canvas(root, width=300, height=100)
        self.canvas.place(x=190, y=30)
        self.img = PhotoImage(file="img_1.png")
        self.canvas.create_image(0, 0, anchor=NW, image=self.img)

        self.num_select1 = Button(root, width=2, bg="gold").place(x=50, y=200)
        self.num_select2 = Button(root, width=2, bg="gold").place(x=100, y=200)
        self.num_select3 = Button(root, width=2, bg="gold").place(x=150, y=200)
        self.num_select4 = Button(root, width=2, bg="gold").place(x=200, y=200)
        self.num_select5 = Button(root, width=2, bg="gold").place(x=250, y=200)
        self.num_select7 = Button(root, width=2, bg="gold").place(x=300, y=200)
        self.num_select8 = Button(root, width=2, bg="gold").place(x=350, y=200)
        self.num_select9 = Button(root, width=2, bg="gold").place(x=50, y=250)
        self.num_select10 = Button(root, width=2, bg="gold").place(x=100, y=250)
        self.num_select11 = Button(root, width=2, bg="gold").place(x=150, y=250)
        self.num_select12 = Button(root, width=2, bg="gold").place(x=200, y=250)
        self.num_select13 = Button(root, width=2, bg="gold").place(x=250, y=250)
        self.num_select14 = Button(root, width=2, bg="gold").place(x=300, y=250)
        self.num_select15 = Button(root, width=2, bg="gold").place(x=350, y=250)
        self.num_select16 = Button(root, width=2, bg="gold").place(x=50, y=300)
        self.num_select17 = Button(root, width=2, bg="gold").place(x=100, y=300)
        self.num_select18 = Button(root, width=2, bg="gold").place(x=150, y=300)
        self.num_select19 = Button(root, width=2, bg="gold").place(x=200, y=300)
        self.num_select20 = Button(root, width=2, bg="gold").place(x=250, y=300)
        self.num_select21 = Button(root, width=2, bg="gold").place(x=300, y=300)
        self.num_select22 = Button(root, width=2, bg="gold").place(x=350, y=300)
        self.num_select23 = Button(root, width=2, bg="gold").place(x=50, y=350)
        self.num_select24 = Button(root, width=2, bg="gold").place(x=100, y=350)
        self.num_select25 = Button(root, width=2, bg="gold").place(x=150, y=350)
        self.num_select26 = Button(root, width=2, bg="gold").place(x=200, y=350)
        self.num_select27 = Button(root, width=2, bg="gold").place(x=250, y=350)
        self.num_select28 = Button(root, width=2, bg="gold").place(x=300, y=350)
        self.num_select29 = Button(root, width=2, bg="gold").place(x=350, y=350)
        self.num_select30 = Button(root, width=2, bg="gold").place(x=50, y=400)
        self.num_select31 = Button(root, width=2, bg="gold").place(x=100, y=400)
        self.num_select32 = Button(root, width=2, bg="gold").place(x=150, y=400)
        self.num_select33 = Button(root, width=2, bg="gold").place(x=200, y=400)
        self.num_select34 = Button(root, width=2, bg="gold").place(x=250, y=400)
        self.num_select35 = Button(root, width=2, bg="gold").place(x=300, y=400)
        self.num_select36 = Button(root, width=2, bg="gold").place(x=350, y=400)
        self.num_select37 = Button(root, width=2, bg="gold").place(x=50, y=450)
        self.num_select38 = Button(root, width=2, bg="gold").place(x=100, y=450)
        self.num_select39 = Button(root, width=2, bg="gold").place(x=150, y=450)
        self.num_select40 = Button(root, width=2, bg="gold").place(x=200, y=450)
        self.num_select41 = Button(root, width=2, bg="gold").place(x=250, y=450)
        self.num_select42 = Button(root, width=2, bg="gold").place(x=300, y=450)
        self.num_select43 = Button(root, width=2, bg="gold").place(x=350, y=450)
        self.num_select44 = Button(root, width=2, bg="gold").place(x=50, y=500)
        self.num_select45 = Button(root, width=2, bg="gold").place(x=100, y=500)
        self.num_select46 = Button(root, width=2, bg="gold").place(x=150, y=500)
        self.num_select47 = Button(root, width=2, bg="gold").place(x=200, y=500)
        self.num_select48 = Button(root, width=2, bg="gold").place(x=250, y=500)
        self.num_select49 = Button(root, width=2, bg="gold").place(x=300, y=500)
        self.num_select50 = Button(root, width=2, bg="gold").place(x=350, y=500)







        x = random.sample(range(1, 49), 6)
        print(x)


Play()

root.mainloop()


x = open("File.txt", 'w')
