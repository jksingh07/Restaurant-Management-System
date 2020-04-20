from tkinter import  *
from tkinter  import messagebox
import time
import sqlite3


#=================CONNECTING WITH THE DATABASE====================================

con = sqlite3.connect('Restaurant.db')
cursor = con.cursor()

#=================SETTING UP FRAME=========================================

root = Tk()
root.geometry("1600x800+0+0")
root.title("JK Restaurant")

top =  Frame(root, width=1600, height=60, bg='powder blue', relief=SUNKEN)
top.pack(side=TOP)

f3 = Frame(root, width=1600, height=200, relief=SUNKEN)
f3.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=800, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)


#==================TIME==========================================
time = time.asctime(time.localtime(time.time()))

#==================TOP FRAME (HEADER)==========================================

l1 = Label(top, font=('arial',40,'bold'), text = 'Restaurant Admin Portal', fg='Steel Blue',bd=10, anchor='w')
l1.grid(row=0, column=0)

l2 = Label(top, font=('arial',20,'bold'), text = time, fg='Steel Blue',bd=10, anchor='w')
l2.grid(row=1, column=0)



#=======================FUNCTIONALITIES=========================================
def search():
    if flag:
        ref_no = int(ref.get())
        cursor.execute("SELECT * FROM customers WHERE id=?",(ref_no,))
        con.commit()
        records = cursor.fetchall()
        if records:
            record = records[0]
            if record[0] == int(ref.get()):
                total.set("Rs. {}".format(record[5]))
                order.set("{0} Fries, {1} Burger, {2} Wrap, {3} Drinks,{4} Sandwich,{5} Meal, {6} Shakes".format(record[6],record[7],record[8],record[9],record[10],record[11],record[12]))

        else:
            order.set("No Order")
            msg = messagebox.showinfo('Error', 'Invalid Reference No.\nRecheck your Reference No. or Place the order again')
            ref.set("")
            order.set("")

    
def reset():
    if flag:
        order.set("")
        ref.set("")
        total.set("")

def change_color():
    pswd_disp.config(bg='powder blue')
    edit_button.config(bg='powder blue')
    del_button.config(bg='powder blue')
    search_button.config(bg='powder blue')
    reset_button.config(bg='powder blue')
    ref_disp.config(bg='powder blue')
    fries_disp.config(bg='powder blue')
    burger_disp.config(bg='powder blue')
    wrap_disp.config(bg='powder blue')
    meal_disp.config(bg='powder blue')
    shakes_disp.config(bg='powder blue')
    drinks_disp.config(bg='powder blue')
    sandwich_disp.config(bg='powder blue')
        

def log_in():
    global flag
    if id_.get() == 'admin' and pswd.get() == '1234':
        msg = messagebox.showinfo('JK Restaurant', 'Succesfully Logged In')
        flag = True
        id_.set("")
        pswd.set("")
        change_color()
                
    else:
        msg = messagebox.showinfo('JK Restaurant', 'Incorrect Id or Password')
        pswd.set("")
        pswd_disp.config(bg='IndianRed')

def edit():
    cost = (int(Fries.get())*50)+(int(burger.get())*100)+(int(Wrap.get())*60)+(int(Drinks.get())*50)+(int(Sandwich.get())*50)+(int(Meal.get())*200)+(int(Shakes.get())*60)
    cgst_sum=cost*0.025
    sgst_sum=cost*0.025
    gst_total=cgst_sum + sgst_sum
    grand_total=cost + gst_total
    total.set(str(grand_total))
    
    cursor.execute("UPDATE customers SET bill_amount=?,fries=?,burger=?,wrap=?,drinks=?,sandwich=?,meal=?,shakes=? WHERE id=?",(grand_total,int(Fries.get()), int(burger.get()), int(Wrap.get()), int(Drinks.get()),int(Sandwich.get()), int(Meal.get()), int(Shakes.get()), int(ref.get())))
    con.commit()
    msg = messagebox.showinfo('JK Restaurant', 'Order Updated Sucessfully')
    Fries.set("")
    burger.set("")
    Wrap.set("")
    Drinks.set("")
    Sandwich.set("")
    Meal.set("")
    Shakes.set("")

def delete():
    cursor.execute("DELETE FROM customers WHERE id=?",(int(ref.get()),))
    con.commit()
    order.set("")
    msg = messagebox.showinfo('JK Restaurant','Order Deleted Sucessfully!!!')

def exit():
    msg = messagebox.showinfo('JK Restaurant', 'Thank You!!! \nHope you enjoyed our services')
    root.destroy()

#=====================LEFT FRAME (FOR ORDERS)====================================
order = StringVar()
ref = StringVar()
total = StringVar()
id_ = StringVar()
pswd = StringVar()
ref=StringVar()
Fries=StringVar()
burger=StringVar()
Wrap=StringVar()
Drinks=StringVar()
Sandwich=StringVar()
Meal=StringVar()
Shakes=StringVar()
flag = False

l3 = Label(f1, text='Reference', font=('arial',20,'bold'),bd=16,anchor='w')
l3.grid(row=0,column=0)

ref_disp = Entry(f1, textvariable=ref, font = ('arial',16,'bold'),bd=16,insertwidth=4,bg='gray40',justify='right')
ref_disp.grid(row=0, column=1)

search_button = Button(f1, text='Search', command=search, bg='gray40',padx=16,pady=5,bd=16,fg='black',font=('arial',16,'bold'),width=10)
search_button.grid(row=1,column=0)

reset_button = Button(f1, text='Reset', command = reset, bg='gray40',padx=16,pady=5,bd=16,fg='black',font=('arial',16,'bold'),width=10)
reset_button.grid(row=1, column=1)



l4 = Label(f1, text='ID', font=('arial',20,'bold'),bd=16, anchor='w')
l4.grid(row=2, column=0)

id_disp = Entry(f1, textvariable=id_, font=('arial',16,'bold'),bd=16,insertwidth=4,bg='powder blue', justify='right')
id_disp.grid(row=2,column=1)

l5 = Label(f1, text='Password', font=('arial',20,'bold'),bd=16, anchor='w')
l5.grid(row=3, column=0)

pswd_disp = Entry(f1, textvariable=pswd, show='*',font=('arial',16,'bold'),bd=16,insertwidth=4,bg='powder blue', justify='right')
pswd_disp.grid(row=3,column=1)

LogIn_button = Button(f1, text='Log In', command=log_in, bg='powder blue',padx=16,pady=5,bd=16, fg='black', font=('arial',16,'bold'), width=10)
LogIn_button.grid(row=4,column=0)

exit_button = Button(f1, text='Exit', command = exit,bg='powder blue', padx=16,pady=5,bd=16, fg='black', font=('arial',16,'bold'), width=10)
exit_button.grid(row=5, column=0)

del_button = Button(f1, text='Delete Order', command = delete, bg='gray40',padx=16,pady=5,bd=16, fg='black', font=('arial',16,'bold'), width=10)
del_button.grid(row=5,column=1)


order_label = Label(f3, text='Your Order: ',font=('arial',20,'bold'),bd=16,anchor='w')
order_label.grid(row=0,column=0)

order_disp = Entry(f3, textvariable=order,font=('arial',20,'bold'),bd=20,insertwidth=4,bg='white',justify='left',width=80)
order_disp.grid(row=0,column=1)

bill_label = Label(f3, text='Total Billing Amount: ',font=('arial',20,'bold'),bd=10,anchor='w')
bill_label.grid(row=1,column=0)

bill_disp = Entry(f3, textvariable=total,font=('arial',14,'bold'),bd=10,insertwidth=3,bg='white',justify='left',width=30)
bill_disp.grid(row=1,column=1)


l6 = Label(f2, text='Fries', font=('arial',20,'bold'),bd=16, anchor='w')
l6.grid(row=0,column=0)

fries_disp = Entry(f2, textvariable=Fries, bg='gray40',font=('arial',10,'bold'),bd=10,insertwidth=1,justify='right')
fries_disp.grid(row=0,column=1)

l7 = Label(f2, text='Burger', font=('arial',20,'bold'),bd=16, anchor='w')
l7.grid(row=0,column=2)

burger_disp = Entry(f2, textvariable=burger, bg='gray40',font=('arial',10,'bold'),bd=10,insertwidth=1,justify='right')
burger_disp.grid(row=0,column=3)

l8 = Label(f2, text='Wrap', font=('arial',20,'bold'),bd=16, anchor='w')
l8.grid(row=1,column=0)

wrap_disp = Entry(f2, textvariable=Wrap, bg='gray40',font=('arial',10,'bold'),bd=10,insertwidth=1,justify='right')
wrap_disp.grid(row=1,column=1)

l8 = Label(f2, text='Drinks', font=('arial',20,'bold'),bd=16, anchor='w')
l8.grid(row=1,column=2)

drinks_disp = Entry(f2, textvariable=Drinks, bg='gray40',font=('arial',10,'bold'),bd=10,insertwidth=1,justify='right')
drinks_disp.grid(row=1,column=3)

l9 = Label(f2, text='Sandwich', font=('arial',20,'bold'),bd=16, anchor='w')
l9.grid(row=2,column=0)

sandwich_disp = Entry(f2, textvariable=Sandwich, bg='gray40',font=('arial',10,'bold'),bd=10,insertwidth=1,justify='right')
sandwich_disp.grid(row=2,column=1)

l10 = Label(f2, text='Meal', font=('arial',20,'bold'),bd=16, anchor='w')
l10.grid(row=2,column=2)

meal_disp = Entry(f2, textvariable=Meal, bg='gray40',font=('arial',10,'bold'),bd=10,insertwidth=1,justify='right')
meal_disp.grid(row=2,column=3)

l11 = Label(f2, text='Shakes', font=('arial',20,'bold'),bd=16, anchor='w')
l11.grid(row=3,column=0)

shakes_disp = Entry(f2, textvariable=Shakes, bg='gray40',font=('arial',10,'bold'),bd=10,insertwidth=1,justify='right')
shakes_disp.grid(row=3,column=1)

edit_button = Button(f2, text='Update Order', command = edit, bg='gray40',padx=16,pady=5,bd=16, fg='black', font=('arial',16,'bold'), width=10)
edit_button.grid(row=4,column=0)


root.mainloop()






