from tkinter import *
from tkinter import messagebox

win = Tk()
win.title('P O S')
win.geometry('500x500')
win.resizable(0,0)

sandwiches = {
    "Kafta": 95000,
    "Shawarma": 85000,
    "Beef Steak": 80000,
    "Tawouk": 85000
}

ordered_items = []
total_price = 0

def add_sandwich(sandwich):
    global total_price
    price = sandwiches[sandwich]
    ordered_items.append((sandwich, price))
    total_price += price
    update_order_list()

def update_order_list():
    listbox.delete(0, END)
    for item, price in ordered_items:
        listbox.insert(END, f"{item}        {price} LBP")
    lb_total.config(text=f"Ordered price: {total_price} LBP")

def new_order():
    global ordered_items, total_price
    ordered_items.clear()
    total_price = 0
    update_order_list()
    v_payment.set("")
    lb_return.config(text="Cash Return: 0 LBP")

def delete_item():
    global total_price
    selected_item = listbox.curselection()
    if selected_item:
        index = selected_item[0]
        item_to_remove = ordered_items.pop(index)
        total_price -= item_to_remove[1]
        update_order_list()

def cash_payment():
    global total_price
    try:
        customer_payment = float(v_payment.get())
        if customer_payment >= total_price:
            cash_return = customer_payment - total_price
            lb_return.config(text=f"Cash Return: {cash_return} LBP")
            messagebox.showinfo("Payment", "Thank You! Come again!")
            new_order()
        else:
            lb_return.config(text="")
            messagebox.showwarning("Payment", "Insufficient Funds")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

listbox = Listbox(win, width=30, height=20)
listbox.place(x=260, y=40)

lb_total = Label(win, text="Ordered price: 0 LBP", font=('Arial', 14))
lb_total.place(x=40, y=260)

lb_return = Label(win, text="Cash Return: 0 LBP", font=('Arial', 14))
lb_return.place(x=40, y=340)

button_kafta = Button(win, text="Kafta", width=11, height=5, command=lambda: add_sandwich("Kafta"))
button_kafta.place(x=40,y=40)

button_shawarma = Button(win, text="Shawarma", width=11, height=5, command=lambda: add_sandwich("Shawarma"))
button_shawarma.place(x=140,y=40)

button_beef = Button(win, text="Beef steak", width=11, height=5, command=lambda: add_sandwich("Beef Steak"))
button_beef.place(x=40,y=140)

button_tawouk = Button(win, text="Tawouk", width=11, height=5, command=lambda: add_sandwich("Tawouk"))
button_tawouk.place(x=140,y=140)

v_payment = StringVar()
entry_payment = Entry(win, textvariable=v_payment, width=30)
entry_payment.place(x=40, y=300)

btn_new_order = Button(win, text="New Order", width=14, height=4, command=new_order, fg= 'red')
btn_new_order.place(x=40, y=400)

btn_delete = Button(win, text="Delete Item", width=14, height=4, command=delete_item, fg= 'red')
btn_delete.place(x=190, y=400)

btn_payment = Button(win, text="Cash Payment", width=14, height=4, command=cash_payment, fg= 'green')
btn_payment.place(x=340, y=400)

win.mainloop()
