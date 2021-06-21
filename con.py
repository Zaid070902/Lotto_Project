from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests

from Random_window import total_list

root = Tk()


root.geometry("450x350")
root.title("Currency")
root.config(bg="#120127")

x = StringVar()
y = StringVar()
z = StringVar()


data = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/ZAR')
info = data.json()

rates = info['conversion_rates']

currency = []
for i in rates.keys():
    currency.append(i)

select_lab = Label(root, text="Select Currency:", bg="#120127", fg="gold", font=25).place(x=10, y=50)
bankz = ["ABSA", "Capitec", "FNB", "African Bank"]
Bank_select = Label(root, text="Select your bank:", bg="#120127", fg="gold", font=25).place(x=10, y=100)
bankzBox = ttk.Combobox(root, values=bankz, width=18).place(x=220, y=100)

currencyBox = ttk.Combobox(root, values=currency, width=18)
currencyBox.place(x=220, y=50)

Label(root, text='Enter Account number:', bg="#120127", fg="gold", font=25).place(x=10, y=10)
amount_ent = Entry(root, bg="#120127", fg="gold")
amount_ent.place(x=220, y=10)
amount_ent.focus()


def convert(change, money):
    amount = round(money * rates[change], 4)
    x.set("R" + str(amount))

    text = ""
    my_file = open("Text_file.txt", 'a')
    text += "Bank: " + bankzBox.get()
    text += '\n'
    text += "Account number: " + amount_ent.get()
    text += '\n'
    my_file.write(text)


def perform():
    try:
        amount = float(sum(total_list))
        to_curr = currencyBox.get()

        converted_amount = convert(to_curr, amount)

        x.set(converted_amount)
    except ValueError:
        if amount_ent != int and amount_ent != float:
            messagebox.showerror('Invalid entry', 'Only enter digits')

    except requests.exceptions.ConnectionError:
        messagebox.showerror('Internet error', 'Internet Bad')
    except KeyError:
        messagebox.showerror('ERROR', 'Select Currency')


def exit():
    root.destroy()


def clear():
    amount_ent.delete(0, END)
    amount_ent.focus()
    x.set('')


Label(root, textvariable=x, bg="#120127", fg="gold").place(x=160, y=150)
Button(root, text="CONVERT", bg="#120127", fg="gold", highlightbackground="gold", command=perform).place(x=10, y=150)
Button(root, text="EXIT", bg="#120127", fg="gold", highlightbackground="gold", command=exit).place(x=10, y=200)
Button(root, text="CLEAR", bg="#120127", fg="gold", highlightbackground="gold", command=clear).place(x=10, y=250)


root.mainloop()
