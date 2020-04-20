#=================RESTAURANT MANAGMENT SYSTEM===============================


from tkinter import *
from tkinter import messagebox
from Restaurant_DB import *
import random
import time
import datetime

con = sql_connection()

root=Tk()
root.geometry("1600x800+0+0")
root.title("JK Restaurant")
text_in=StringVar()
operator=""
file=open("restaurant.txt",'a+')

top=Frame(root, width=1600,height=50,bg="powder blue", relief=SUNKEN)
top.pack(side=TOP)

f1=Frame(root, width=800,height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root, width=300,height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

#=======================TIME========================================================
time=time.asctime(time.localtime(time.time()))

#======================INFO====================================================
l1=Label(top,font=("arial",50,"bold"),text="Restaurant Billing system",fg='Steel Blue',bd=10,anchor='w')
l1.grid(row=0,column=0)

l2=Label(top,font=("arial",20,"bold"),text=time,fg='Steel Blue',bd=10,anchor='w')
l2.grid(row=1,column=0)


#====================CALCULATOR================================================

def button_click(num):
    global operator
    operator+= str(num)
    text_in.set(operator)
    
def compute():
    global operator
    result=str(eval(operator))
##    print(str(eval(Display.get())))
##    if operator=='':
##        result=str(eval(Display.get()))
##        text_in.set()
##        operator=result
    text_in.set(result)
    operator=result

def clear():
    global operator
    operator=""
    text_in.set(operator)


def Ref():
    x=random.randint(12900,30900)
    random_ref=str(x)
    ref.set(random_ref)

    if Fries.get()=='':
        Fries.set('0')

    if burger.get()=='':
        burger.set('0')

    if Wrap.get()=='':
        Wrap.set('0')

    if Drinks.get()=='':
        Drinks.set('0')

    if Sandwich.get()=='':
        Sandwich.set('0')

    if Meal.get()=='':
        Meal.set('0')

    if Shakes.get()=='':
        Shakes.set('0')
    

    total=(int(Fries.get())*50)+(int(burger.get())*100)+(int(Wrap.get())*60)+(int(Drinks.get())*50)+(int(Sandwich.get())*50)+(int(Meal.get())*200)+(int(Shakes.get())*60)
    cost.set(str(total))

    cgst_sum=total*0.025
    sgst_sum=total*0.025
    gst_total=cgst_sum + sgst_sum
    grand_total=total + gst_total
    cgst.set(str(cgst_sum))
    sgst.set(str(sgst_sum))
    sub_total.set("+"+str(gst_total))
    Total.set(str(grand_total))

def submit():
    # INSERTION IN DATABASE
    id_ = int(ref.get())
    contact = int(c_no.get())
    amount = float(Total.get())

    print(int(Fries.get()), int(burger.get()), int(Wrap.get()), int(Drinks.get()),int(Sandwich.get()), int(Meal.get()), int(Shakes.get())) 
    
    sql_insert_values(con, id_, datetime.datetime.now(), Name.get(), contact, email.get(), amount, int(Fries.get()), int(burger.get()), int(Wrap.get()), int(Drinks.get()),int(Sandwich.get()), int(Meal.get()), int(Shakes.get()))

    # INSERTION IN FILE
    file.write(ref.get()+','+Name.get()+','+c_no.get()+','+email.get()+','+Total.get()+'\n')
    msg=messagebox.showinfo('JK Restaurant','Order Confirmed\nTell your Reference no. at counter to  collect your order')
    reset()
    

def qExit():
    msg = messagebox.showinfo('JK Restaurant', 'Thank You!!! \nHope you enjoyed our services')
    root.destroy()

def reset():
    Name.set("")
    c_no.set("")
    email.set("")
    cost.set("")
    cgst.set("")
    sgst.set("")
    sub_total.set("")
    Total.set("")
    ref.set("")
    Fries.set("")
    burger.set("")
    Wrap.set("")
    Drinks.set("")
    Sandwich.set("")
    Meal.set("")
    Shakes.set("")

        
#=========================CALCULATOR KEYBOARD=============================================
Display=Entry(f2,textvariable=text_in,font=("arial",20,"bold"),bg='powder blue',justify='right',bd=10,insertwidth=10,width=21)
Display.grid(columnspan=4)

btn7=Button(f2,padx=14,pady=16,text='7',command=lambda:button_click(7),fg='black',bg='powder blue',font=('arial',20,'bold'),bd=8).grid(row=2,column=0)
btn8=Button(f2,padx=14,pady=16,text='8',command=lambda:button_click(8),fg='black',bg='powder blue',font=('arial',20,'bold'),bd=8).grid(row=2,column=1)
btn9=Button(f2,padx=14,pady=16,text='9',command=lambda:button_click(9),fg='black',bg='powder blue',font=('arial',20,'bold'),bd=8).grid(row=2,column=2)
btn_sub=Button(f2,padx=14,pady=16,text='-',command=lambda:button_click('-'),fg='black',bg='powder blue',font=('arial',20,'bold'),bd=8).grid(row=2,column=3)
btn_add=Button(f2,padx=14,pady=64,text='+',command=lambda:button_click('+'),fg='black',bg='powder blue',font=('arial',20,'bold'),bd=8).grid(rowspan=2,column=3)
btn4=Button(f2,padx=14,pady=16,text='4',command=lambda:button_click(4),fg='black',bg='powder blue',font=('arial',20,'bold'),bd=8).grid(row=3,column=0)
btn5=Button(f2,padx=14,pady=16,text='5',command=lambda:button_click(5),fg='black',bg='powder blue',font=('arial',20,'bold'),bd=8).grid(row=3,column=1)
btn6=Button(f2,padx=14,pady=16,text='6',command=lambda:button_click(6),fg='black',bg='powder blue',font=('arial',20,'bold'),bd=8).grid(row=3,column=2)
btn1=Button(f2,padx=14,pady=16,text='1',command=lambda:button_click(1),fg='black',bg='powder blue',font=('arial',20,'bold'),bd=8).grid(row=4,column=0)
btn2=Button(f2,padx=14,pady=16,text='2',command=lambda:button_click(2),fg='black',bg='powder blue',font=('arial',20,'bold'),bd=8).grid(row=4,column=1)
btn3=Button(f2,padx=14,pady=16,text='3',command=lambda:button_click(3),fg='black',bg='powder blue',font=('arial',20,'bold'),bd=8).grid(row=4,column=2)
btn0=Button(f2,padx=60,pady=16,text='0',command=lambda:button_click(0),fg='black',bg='powder blue',font=('arial',20,'bold'),bd=8).grid(row=5,columnspan=2)
btn_=Button(f2,padx=16,pady=16,text='.',command=lambda:button_click('.'),fg='black',bg='powder blue',font=('arial',20,'bold'),bd=8).grid(row=5,column=2)
btn_mult=Button(f2,padx=16,pady=16,text='*',command=lambda:button_click('*'),fg='black',bg='powder blue',font=('arial',20,'bold'),bd=8).grid(row=5,column=3)
btn_equal=Button(f2,padx=64,pady=16,command=compute,text='=',fg='black',bg='powder blue',font=('arial',20,'bold'),bd=8).grid(row=6,columnspan=2)
btn_C=Button(f2,padx=16,pady=16,command=clear,text='C',bd=8,fg='black',bg='powder blue',font=('arial',20,'bold')).grid(row=6,column=2)
btn_div=Button(f2,padx=16,pady=16,text='/',command=lambda:button_click('/'),fg='black',bg='powder blue',font=('arial',20,'bold'),bd=8).grid(row=6,column=3)

#========================================RESTAURANT INFO 1================================================
ref=StringVar()
Fries=StringVar()
burger=StringVar()
Wrap=StringVar()
Drinks=StringVar()
Sandwich=StringVar()
Meal=StringVar()
Shakes=StringVar()

l_ref=Label(f1,text="Reference",font=('arial',16,'bold'),bd=16,anchor='w').grid(row=0,column=0)
txt_ref=Entry(f1,textvariable=ref,font=('arial',16,'bold'),bd=16,insertwidth=4,bg='powder blue',justify='right').grid(row=0,column=1)

l_fries=Label(f1,text="Fries (Rs.50)",font=('arial',16,'bold'),bd=16,padx=27,anchor='w').grid(row=1,column=0)
txt_Fries=Entry(f1,textvariable=Fries,font=('arial',16,'bold'),bd=16,insertwidth=4,bg='powder blue',justify='right').grid(row=1,column=1)

l_burger=Label(f1,text="Burger Meal (Rs.100)",font=('arial',16,'bold'),bd=16,anchor='w').grid(row=2,column=0)
txt_burger=Entry(f1,textvariable=burger,font=('arial',16,'bold'),bd=16,insertwidth=4,bg='powder blue',justify='right').grid(row=2,column=1)

l_Wrap=Label(f1,text=" Veg/Chicken Wrap(Rs.50)",font=('arial',16,'bold'),bd=16,anchor='w').grid(row=3,column=0)
txt_Wrap=Entry(f1,textvariable=Wrap,font=('arial',16,'bold'),bd=16,insertwidth=4,bg='powder blue',justify='right').grid(row=3,column=1)

l_Drinks=Label(f1,text=" Soft Drinks(Rs.60)",font=('arial',16,'bold'),bd=16,anchor='w').grid(row=4,column=0)
txt_Drinks=Entry(f1,textvariable=Drinks,font=('arial',16,'bold'),bd=16,insertwidth=4,bg='powder blue',justify='right').grid(row=4,column=1)

l_Sandwich=Label(f1,text="Veg/Chicken Sandwich(Rs.50)",font=('arial',16,'bold'),bd=16,anchor='w').grid(row=5,column=0)
txt_Sandwich=Entry(f1,textvariable=Sandwich,font=('arial',16,'bold'),bd=16,insertwidth=4,bg='powder blue',justify='right').grid(row=5,column=1)

l_meal=Label(f1,text="Super Value Meal(Rs.200)",font=('arial',16,'bold'),bd=16,anchor='w').grid(row=6,column=0)
txt_Meal=Entry(f1,textvariable=Meal,font=('arial',16,'bold'),bd=16,insertwidth=4,bg='powder blue',justify='right').grid(row=6,column=1)

l_shakes=Label(f1,text="Thick Shakes(Rs.60)",font=('arial',16,'bold'),bd=16,anchor='w').grid(row=7,column=0)
txt_Shakes=Entry(f1,textvariable=Shakes,font=('arial',16,'bold'),bd=16,insertwidth=4,bg='powder blue',justify='right').grid(row=7,column=1)


#=================================================RESTAURANT INFO 2==================================================

Name=StringVar()
c_no=StringVar()
email=StringVar()
cost=StringVar()
cgst=StringVar()
sgst=StringVar()
sub_total=StringVar()
Total=StringVar()


l_Name=Label(f1,text="Name",font=('arial',16,'bold'),bd=16,anchor='w').grid(row=0,column=2)
txt_Filet_o_meal=Entry(f1,textvariable=Name,font=('arial',16,'bold'),bd=16,insertwidth=4,bg='white',justify='right').grid(row=0,column=3)

l_c_no=Label(f1,text="Contact No.",font=('arial',16,'bold'),bd=16,padx=27,anchor='w').grid(row=1,column=2)
txt_c_no=Entry(f1,textvariable=c_no,font=('arial',16,'bold'),bd=16,insertwidth=4,bg='white',justify='right').grid(row=1,column=3)

l_email=Label(f1,text="Email-Id",font=('arial',16,'bold'),bd=16,anchor='w').grid(row=2,column=2)
txt_email=Entry(f1,textvariable=email,font=('arial',16,'bold'),bd=16,insertwidth=4,bg='white',justify='right').grid(row=2,column=3)

l_cost=Label(f1,text="Cost",font=('arial',16,'bold'),bd=16,anchor='w').grid(row=3,column=2)
txt_cost=Entry(f1,textvariable=cost,font=('arial',16,'bold'),bd=16,insertwidth=4,bg='white',justify='right').grid(row=3,column=3)

l_cgst=Label(f1,text="C.G.S.T",font=('arial',16,'bold'),bd=16,anchor='w').grid(row=4,column=2)
txt_cgst=Entry(f1,textvariable=cgst,font=('arial',16,'bold'),bd=16,insertwidth=4,bg='white',justify='right').grid(row=4,column=3)

l_sgst=Label(f1,text="S.G.S.T",font=('arial',16,'bold'),bd=16,anchor='w').grid(row=5,column=2)
txt_sgst=Entry(f1,textvariable=sgst,font=('arial',16,'bold'),bd=16,insertwidth=4,bg='white',justify='right').grid(row=5,column=3)

l_sub_total=Label(f1,text="Sub Total",font=('arial',16,'bold'),bd=16,anchor='w').grid(row=6,column=2)
txt_sub_total=Entry(f1,textvariable=sub_total,font=('arial',16,'bold'),bd=16,insertwidth=4,bg='white',justify='right').grid(row=6,column=3)

l_Total=Label(f1,text="Total Cost",font=('arial',16,'bold'),bd=16,anchor='w').grid(row=7,column=2)
txt_Total=Entry(f1,textvariable=Total,font=('arial',16,'bold'),bd=16,insertwidth=4,bg='white',justify='right').grid(row=7,column=3)


#=================================BUTTONS======================================================


btnTotal=Button(f1,text='Total',command=Ref,bg='powder blue',padx=16,pady=5,bd=16,fg='black',font=('arial',16,'bold'),width=10).grid(row=8,column=0)
btnrReset=Button(f1,text='Reset',command=reset,bg='powder blue',padx=16,pady=5,bd=16,fg='black',font=('arial',16,'bold'),width=10).grid(row=8,column=1)
btnqExit=Button(f1,text='Exit',command=qExit,bg='powder blue',padx=16,pady=5,bd=16,fg='black',font=('arial',16,'bold'),width=10).grid(row=8,column=2)
btnSubmit=Button(f1,text='Submit',command=submit,bg='powder blue',padx=16,pady=5,bd=16,fg='black',font=('arial',16,'bold'),width=10).grid(row=8,column=3)






root.mainloop()
file.close()
