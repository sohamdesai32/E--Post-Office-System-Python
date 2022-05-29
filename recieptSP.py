import random
from tkinter import *
from tkinter import messagebox

from geopy.distance import distance
from geopy.geocoders import Nominatim
from mysql.connector import *


class RecieptSP:
    def __init__(self, user_name):
        self.user_name = user_name

        reciept_window1 = Tk()
        reciept_window1.title("Reciept")
        reciept_window1.geometry("500x500")
        reciept_window1.configure(background='cyan')

        label1 = Label(reciept_window1, text="Reciept", font=("Arial Bold", 20), bg='cyan')
        label1.pack(fill=X)

        conn = connect(host='localhost', database='python_mini_project', user='root', password='')
        cursor = conn.cursor()
        cursor.execute("select * from packagesSP where user_name = '" + user_name + "'")
        data = cursor.fetchall()
        for row in data:
            name = row[1]
            phone = row[3]
            weight = row[5]
            address = row[4]
            order_no = row[0]

            name_label = Label(reciept_window1, text=f"Name: {name}", font=("Arial", 20), bg='cyan')
            name_label.place(x=10, y=40)

            phone_label = Label(reciept_window1, text=f"Phone: {phone}", font=("Arial", 20), bg='cyan')
            phone_label.place(x=10, y=80)

            weight_label = Label(reciept_window1, text=f"Weight: {weight}", font=("Arial", 20), bg='cyan')
            weight_label.place(x=10, y=130)

            address_label = Label(reciept_window1, text=f"Address: {address}", font=("Arial", 20), bg='cyan')
            address_label.place(x=10, y=180)

            order_no_label = Label(reciept_window1, text=f"Order No: {order_no}", font=("Arial", 20), bg='cyan')
            order_no_label.place(x=10, y=270)

        cursor.execute("select * from paymentSP where user_name = '" + user_name + "'")
        data1 = cursor.fetchall()
        for row in data1:
            price = row[7]

            price_label = Label(reciept_window1, text=f"Total Price: {price}", font=("Arial", 20), bg='cyan')
            price_label.place(x=10, y=320)

        reciept_window1.mainloop()


if __name__ == "__main__":
    RecieptSP("")
