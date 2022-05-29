from datetime import datetime
from random import randint
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import askyesno

from mysql.connector import *


class Package_SP:
    def __init__(self, user_name):
        self.user_name = user_name

        SP = Tk()
        SP.title("Speed Post")
        SP.configure(background='#00BFFF')
        SP.geometry("650x500+300+100")
        label = Label(SP, text="Speed Post", font=("times new roman", 25, "bold"), bg="red", fg="black")
        label.pack(fill=X)
        reciever_name = Label(SP, text="Reciever's Name :", font=("times new roman", 17, "bold"), bg="#00BFFF",
                              fg="black")
        reciever_name.place(x=20, y=70)
        reciever_name_entry = Entry(SP, width=30)
        reciever_name_entry.place(x=220, y=75)
        reciever_address = Label(SP, text="Reciever's Address :", font=("times new roman", 17, "bold"), bg="#00BFFF",
                                 fg="black")
        reciever_address.place(x=20, y=120)
        reciever_address_entry = Entry(SP, width=30)
        reciever_address_entry.place(x=220, y=122, height=50)
        reciever_phone = Label(SP, text="Reciever's Phone\n Number :", font=("times new roman", 17, "bold"),
                               bg="#00BFFF",
                               fg="black")
        reciever_phone.place(x=20, y=200)
        reciever_phone_entry = Entry(SP, width=30)
        reciever_phone_entry.place(x=220, y=205)
        weight = Label(SP, text="Weight :", font=("times new roman", 17, "bold"), bg="#00BFFF", fg="black")
        weight.place(x=20, y=260)
        weight = ttk.Combobox(SP, values=["0-1 kg", "1-2 kgs", "2-3 kgs", "3-4 kgs", "4-5 kgs"], width=10)
        weight.place(x=220, y=262)

        current_city = Label(SP, text="Current City :", font=("times new roman", 17, "bold"), bg="#00BFFF", fg="black")
        current_city.place(x=20, y=320)
        current_city_entry = Entry(SP, width=30)
        current_city_entry.place(x=220, y=325)
        destination_city = Label(SP, text="Destination City :", font=("times new roman", 17, "bold"), bg="#00BFFF",
                                 fg="black")
        destination_city.place(x=20, y=380)
        destination_city_entry = Entry(SP, width=30)
        destination_city_entry.place(x=220, y=385)

        def send():
            try:
                conn = connect(host="localhost", user="root", passwd="", database="python_mini_project")
                cursor = conn.cursor()
                a = randint(100, 999)
                query = "INSERT INTO packagesSP VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
                data = (a, user_name, reciever_name_entry.get(), reciever_phone_entry.get(), reciever_address_entry.get(), weight.get(), current_city_entry.get(), destination_city_entry.get())
                cursor.execute(query, data)
                if reciever_name_entry.get() == "" or reciever_address_entry.get() == "" or reciever_phone_entry.get() == "" or weight.get() == "" or current_city_entry.get() == "" or destination_city_entry.get() == "":
                    messagebox.showinfo("Error", "Please fill all the fields")
                else:
                    messagebox.showinfo("Success", "Redirecting to your payment dashboard")
                    SP.destroy()
                    import payment_SP
                    payment_SP.PaymentSP(user_name)
            except Exception as e:
                print(e)

        def back1():
            SP.destroy()
            import home
            home.Home(user_name=user_name)

        button = Button(SP, text="Place", font=("times new roman", 15, "bold"), bg="#00BFFF", fg="black",
                        command=send)
        button.place(x=200, y=450)
        back = Button(SP, text="Back", font=("times new roman", 15, "bold"), bg="#00BFFF", fg="black",
                      command=back1)
        back.place(x=300, y=450)
        SP.mainloop()


if __name__ == "__main__":
    Package_SP("")
