import sqlite3
from sqlite3 import Error
import datetime

###########  CREATING SQLite CONNECTION WITH DATABASE ############################

def sql_connection():
    try:
        con = sqlite3.connect('Restaurant.db')
        return con
    except Error:
        print(Error)

def sql_table(con):
    cursor_obj = con.cursor()
    cursor_obj.execute("CREATE TABLE customers(id integer, Date_ timestamp, name text,contact_no integer, email text, bill_amount float, fries integer, burger integer, wrap integer, drinks integer, sandwich integer, meal integer, shakes integer)")
    con.commit()

def sql_insert_values(con, id_, today_date, name, c_no, email, amount, fries, burger, wrap, drinks, sandwich, meal, shakes):
    cursor_obj = con.cursor()
    cursor_obj.execute("INSERT INTO customers VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(id_, today_date, name, c_no, email, amount, fries, burger, wrap, drinks, sandwich, meal, shakes))
    con.commit()


##con = sql_connection()
###sql_table(con)
##
##id_ = 3452
##name = 'JK'
##c_no = 8178896538
##email = 'jksingh.js7@gmail.com'
##amount = 500.0
##fries = 1
##burger = 1
##wrap = 0
##drinks = 2
##sandwich = 1
##meal = 0
##shakes = 0
##today_date = datetime.datetime.now()
##today_date = (today_date,)
##
##sql_insert_values(con, id_, datetime.datetime.now(), name, c_no, email, amount,fries, burger, wrap, drinks, sandwich, meal, shakes)
