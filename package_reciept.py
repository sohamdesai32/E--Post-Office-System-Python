from tkinter import *
from mysql.connector import *


class Receipt:
    def __init__(self, username):
        self.username = username

        receipt_window = Tk()
        receipt_window.title("Receipt")
        receipt_window.geometry("600x650+500+60")
        receipt_window.configure(background='cyan')

        title = Label(receipt_window, text="RECEIPT", font=("Arial", 20, "bold"), bg="cyan", fg="black")
        title.pack(pady=10)
        conn = connect(host='localhost', database='python_mini_project', user='root', password='')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM packages WHERE sender_name = '" + username + "'")
        result = cursor.fetchall()
        for row in result:
            id11 = row[0]
            name = row[1]
            phone = row[3]
            type_pack = row[5]
            address = row[10]

            id2 = Label(receipt_window, text=f"Package ID:{id11}", font=("Arial", 15, "bold"), bg="cyan",
                        fg="black")
            id2.place(x=100, y=70)
            sender_name_label = Label(receipt_window, text=f"Sender Name:{name}", font=("Arial", 15, "bold"),
                                      bg="cyan", fg="black")
            sender_name_label.place(x=100, y=110)
            phone_label = Label(receipt_window, text=f"Phone:{phone}", font=("Arial", 15, "bold"), bg="cyan",
                                fg="black")
            phone_label.place(x=100, y=160)

            address_label = Label(receipt_window, text=f"Address:{address}", font=("Arial", 15, "bold"),
                                  bg="cyan",
                                  fg="black")
            address_label.place(x=100, y=200)

            pack_type_label = Label(receipt_window, text=f"Package Type:{type_pack}", font=("Arial", 15, "bold"),
                                    bg="cyan",
                                    fg="black")
            pack_type_label.place(x=100, y=250)

        cursor.execute("SELECT * FROM payment WHERE user_name = '" + username + "'")
        res = cursor.fetchall()
        for row in res:
            weight = row[2]
            price = row[5]
            total_price = row[6]

            weight_label = Label(receipt_window, text=f"Weight:{weight}", font=("Arial", 15, "bold"), bg="cyan",
                                 fg="black")
            weight_label.place(x=100, y=300)
            price_label = Label(receipt_window, text=f"Price:{price}", font=("Arial", 15, "bold"), bg="cyan",
                                fg="black")
            price_label.place(x=100, y=350)

            total_price_label = Label(receipt_window, text=f"Total Price (with Taxes): {total_price}",
                                      font=("Arial", 15, "bold"),
                                      bg="cyan", fg="black")

            total_price_label.place(x=100, y=400)

        def back():
            receipt_window.destroy()
            import home
            home.Home(username)
        button = Button(receipt_window, text="Back", font=("Arial", 15, "bold"), bg="black", fg="white",
                        command=back)
        button.place(x=250, y=520)
        receipt_window.mainloop()


if __name__ == '__main__':
    Receipt("")
