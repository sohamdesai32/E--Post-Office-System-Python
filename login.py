from tkinter import *
from tkinter import messagebox
from mysql.connector import *


class Login:
    def __init__(self, user_name, password1):
        self.user_name = user_name
        self.password = password1
        root = Tk()
        root.title("Login")
        root.geometry("500x300")
        root.configure(background="light blue")

        title = Label(root, text="Login Page", font=("arial", 20, "bold"), bg="light blue")
        title.place(x=250, y=15)

        username = StringVar()
        password = StringVar()
        username_entry = Entry(root, width=30, textvariable=username)
        password_entry = Entry(root, width=30, textvariable=password, show="*")
        user = Label(root, text="Username:", font=("arial", 10, "bold"), bg="light blue")
        passw = Label(root, text="Password:", font=("arial", 10, "bold"), bg="light blue")
        user.place(x=180, y=100)
        passw.place(x=180, y=150)
        username_entry.place(x=270, y=100)
        password_entry.place(x=270, y=150)
        image = PhotoImage(file="download.png")
        image_label = Label(root, image=image, width=150, height=150)
        image_label.place(x=10, y=50)

        checkbox1 = IntVar()

        def show():
            if checkbox1.get() == 1:
                password_entry.config(show="")
            else:
                password_entry.config(show="*")

        checkbox = Checkbutton(root, text="Show Password", variable=checkbox1, command=show, font=("arial", 10, "bold"),
                               bg="light blue")
        checkbox.place(x=270, y=200)

        def submit():
            try:
                conn = connect(host="localhost", user="root", passwd="", database="python_mini_project")
                cursor = conn.cursor()
                statement = f"SELECT username from users WHERE username='{username_entry.get()}' AND passw = '{password_entry.get()}';"
                cursor.execute(statement)
                result = cursor.fetchall()
                if username.get() == "" or password.get() == "":
                    messagebox.showerror("Error", "Please enter username and password")
                elif len(result) == 0:
                    messagebox.showerror("Error", "Invalid username or password")
                else:
                    messagebox.showinfo("Success", "Login Successful")
                    root.destroy()
                    import home
                    home.Home(username, password)

            except Error as e:
                print(e)

        def SIgnup():
            root.destroy()
            import signup
            signup.Signup()

        submit = Button(root, text="Submit", font=("arial", 10, "bold"), bg="light blue", command=submit)
        submit.place(x=250, y=250)
        signup = Button(root, text="Sign Up", font=("arial", 10, "bold"), bg="light blue", command=SIgnup)
        signup.place(x=330, y=250)
        cancel = Button(root, text="Cancel", font=("arial", 10, "bold"), bg="light blue", command=root.destroy)
        cancel.place(x=410, y=250)
        root.mainloop()


if __name__ == '__main__':
    l = Login(user_name="", password1="")
