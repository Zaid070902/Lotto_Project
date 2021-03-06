from tkinter import *
import rsaidnumber
from datetime import datetime, timedelta
from tkinter import messagebox
from email_validator import validate_email, EmailNotValidError

master = Tk()
master.geometry("600x500")
master.config(bg="#111")

canvas = Canvas(master, width=300, height=100)
canvas.place(x=150, y=10)
img = PhotoImage(file="img_1.png")
canvas.create_image(0, 0, anchor=NW, image=img)

name_lab = Label(master, text="Enter name:", bg="#111", fg="gold", font=15)
name_lab.place(x=100, y=150)

name_ent = Entry(master)
name_ent.place(x=300, y=150)

email_lab = Label(master, text="Enter email address:", bg="#111", fg="gold", font=15)
email_lab.place(x=100, y=200)

email_ent = Entry(master)
email_ent.place(x=300, y=200)

id_num_lab = Label(master, text="Enter ID number:", bg="#111", fg="gold", font=15)
id_num_lab.place(x=100, y=250)

id_num_ent = Entry(master)
id_num_ent.place(x=300, y=250)

address_lab = Label(master, text="Enter address:", bg="#111", fg="gold", font=15)
address_lab.place(x=100, y=300)

address_ent = Entry(master)
address_ent.place(x=300, y=300)


def sub():
    # adding contents to a text file
    text = ""
    my_file = open("Text_file.txt", 'a')
    text += "Username: " + name_ent.get()
    text += '\n'
    text += "Email: " + email_ent.get()
    text += '\n'
    text += "Address: " + address_ent.get()
    text += '\n'
    text += "ID number: " + id_num_ent.get()
    text += '\n'
    my_file.write(text)

    # verifying id number and checking age
    id_num = rsaidnumber.parse(id_num_ent.get())
    age = ((datetime.today() - id_num.date_of_birth) // timedelta(days=365.25))
    if age >= 18:
        messagebox.showinfo("Let's Play")
    else:
        years_left = 18 - age
        messagebox.showinfo("Error", "Return in" + '\n' + str(years_left) + "years time")

    # checking if email is valid
    try:
        validate_email(email_ent.get())

    except EmailNotValidError:
        # email is not valid
        messagebox.showinfo("Invalid Email. Try again")
    master.destroy()
    import Random_window


sub_btn = Button(master, text="Submit", width=10, height=2, bg="#111", fg="gold", font=15, command=sub)
sub_btn.place(x=230, y=350)


master.mainloop()
