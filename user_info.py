from tkinter import *
from tkinter import messagebox
from mysql.connector import *


class User_info:
    def __init__(self, user_name):
        self.user_name = user_name
        user_info = Tk()
        user_info.title("User Info")
        user_info.geometry("600x600")
        user_info.configure(background='#00BFFF')
        label = Label(user_info, text="User Info", bg="light blue", fg="white", font=("Times", 30, "bold"))
        label.pack(side=TOP, fill=X)

        try:
            conn = connect(host="localhost", user="root", passwd="", database="python_mini_project")
            cursor = conn.cursor()
            statement = f"select * from users where username = '{self.user_name}' "
            cursor.execute(statement)
            result = cursor.fetchall()
            for row in result:
                name = row[1]
                phone = row[3]
                email = row[2]
                address = row[6]
                label1 = Label(user_info, text=f"Name : {name}", bg="light blue", fg="black",
                               font=("Times", 15, "bold"))
                label1.place(x=100, y=100)
                label2 = Label(user_info, text=f"Phone No: {phone}", bg="light blue", fg="black",
                               font=("Times", 15, "bold"))
                label2.place(x=350, y=100)
                label7 = Label(user_info, text=f"Email: {email}", bg="light blue", fg="black",
                               font=("Times", 15, "bold"))
                label7.place(x=100, y=150)
                label8 = Label(user_info, text=f"Address : {address}", bg="light blue", fg="black",
                               font=("Times", 15, "bold"))
                label8.place(x=100, y=200)
        except Error as e:
            print(e)

        def back():
            user_info.destroy()
            import home
            home.Home(user_name)

        button = Button(user_info, text="Back", bg="light blue", fg="black", font=("Times", 15, "bold"), command=back)
        button.place(x=100, y=500)

        user_info.mainloop()


if __name__ == "__main__":
    User_info(user_name="")
