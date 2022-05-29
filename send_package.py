from datetime import datetime
from random import randint
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import askyesno
from mysql.connector import *


class Package:
    def __init__(self, user_name):
        self.user_name = user_name
        package = Tk()
        package.title("Send a Package")
        package.geometry("850x650+300+100")
        package.configure(background='cyan')
        label = Label(package, text="SEND A PACKAGE", font=("TIMES NEW ROMAN", 20), bg='cyan')
        label.place(x=300, y=10)
        name_receiver = Label(package, text="Enter the name of \n the recipient:", font=("Helvetica", 15), bg='cyan')
        name_receiver.place(x=10, y=70)
        name_sender = Entry(package, width=25)
        name_sender.place(x=200, y=85)
        name_pack = Label(package, text="Enter the \n package name:", font=("Helvetica", 15), bg='cyan')
        name_pack.place(x=400, y=75)
        name_recipient = Entry(package, width=25)
        name_recipient.place(x=560, y=90)
        email = Label(package, text="Enter the \n recipient phone number:", font=("Helvetica", 15), bg='cyan')
        email.place(x=470, y=150)
        recipient = Entry(package, width=18)
        recipient.place(x=700, y=178)
        type_pack = Label(package, text="Enter the type of package:", font=("Helvetica", 15), bg='cyan')
        type_pack.place(x=10, y=160)
        option = ttk.Combobox(package, width=25, height=5,
                              values=["letter", "Parcel", "Envelope", "Box"])
        option.place(x=260, y=165)
        weight_label = Label(package, text="Enter the weight of package:", font=("Helvetica", 15), bg='cyan')
        weight_label.place(x=470, y=325)
        email = Label(package, text="Enter the \n recipient email:", font=("Helvetica", 15), bg='cyan')
        email.place(x=467, y=255)
        recipient_mail = Entry(package, width=30)
        recipient_mail.place(x=620, y=282)
        weight = ttk.Combobox(package, width=5, values=["0-0.5", "0.6-2", "3-6", "7-10"])
        weight.place(x=730, y=330)
        kg = Label(package, text="kgs", font=("Helvetica", 15), bg='cyan')
        kg.place(x=790, y=325)
        address = Label(package, text="Enter the address of recipient:", font=("Helvetica", 15), bg='cyan')
        address.place(x=10, y=370)
        address = Entry(package, width=50)
        address.place(x=10, y=400, height=150)
        curr_city = Label(package, text="Enter your current city:", font=("Helvetica", 15), bg='cyan')
        curr_city.place(x=10, y=250)
        my_city = Entry(package, width=25)
        my_city.place(x=260, y=255)
        dest_city = Label(package, text="Enter the destination city:", font=("Helvetica", 15), bg='cyan')
        dest_city.place(x=10, y=320)
        dest_city = Entry(package, width=20)
        dest_city.place(x=260, y=325)

        def Quit():
            ans = askyesno("Quit", "Do you want to quit?")
            if ans:
                package.destroy()
            else:
                pass

        cancel = Button(package, text="Cancel", font=("times new roman", 15, "bold"), bg="white", fg="black",
                        command=Quit)
        cancel.place(x=480, y=560)

        def send_package():
            try:
                a = randint(1000, 9999)
                con = connect(host="localhost", user="root", password="", database="python_mini_project")
                cur = con.cursor()
                query = "insert into packages values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                data = (str(a), str(name_sender.get()), str(recipient_mail.get()), str(recipient.get()), str(user_name),
                        str(option.get()), str(name_recipient.get()), str(weight.get()), str(my_city.get()),
                        str(dest_city.get()), str(address.get()))
                cur.execute(query, data)
                if name_sender.get() == "" or recipient_mail.get() == "" or recipient.get() == "" or weight.get() == "" or address.get() == "":
                    messagebox.showinfo("Error", "Please fill all the fields")
                else:
                    messagebox.showinfo("Success", "Successful!! \n Redirecting to your payment dashboard")
                    package.destroy()
                    import paymenet_package
                    paymenet_package.Payment(user_name)

            except Exception as e:
                print(e)

        def back1():
            package.destroy()
            import home
            home.Home(user_name=user_name)

        button = Button(package, text="Place", font=("times new roman", 15, "bold"), bg="white", fg="black",
                        command=send_package)
        button.place(x=300, y=560)
        back = Button(package, text="Back", font=("times new roman", 15, "bold"), fg="black",
                      command=back1)
        back.place(x=380, y=560)
        package.mainloop()


if __name__ == "__main__":
    Package(user_name="")
