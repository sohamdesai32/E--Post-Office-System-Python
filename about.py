from tkinter import *
from tkinter import messagebox
from mysql.connector import *


class About:
    def __init__(self, username):
        self.username = username
        about_us = Tk()
        about_us.title("About Us")
        about_us.geometry("500x600")
        about_us.configure(background='#00BFFF')
        label = Label(about_us, text="About Us", bg="light blue", fg="white", font=("Times", 30, "bold"))
        label.pack(side=TOP, fill=X)
        label1 = Label(about_us, text="This is a simple project to show the use of Tkinter", bg="light blue")
        label1.pack(side=TOP, fill=X)
        label2 = Label(about_us, text="This project is made by:", bg="light blue")
        label2.pack(side=TOP, fill=X)
        label3 = Label(about_us, text="1. Soham\n 2.Dhruv\n 3.Falguni", bg="light blue")
        label3.pack(side=TOP, fill=X)
        label4 = Label(about_us, text="You can follow us on instagram at \n @sohamdesai32 \n @falguni_0803 \n @_dhruv_agrawal_", bg="light blue")
        label4.pack(side=TOP, fill=X)
        label3.pack(side=TOP, fill=X)

        def back():
            about_us.destroy()
            import home
            home.Home(user_name="")

        button = Button(about_us, text="OK", command=back)
        button.place(x=200, y=500, width=100, height=50)

        about_us.mainloop()


if __name__ == '__main__':
    About(username="")
