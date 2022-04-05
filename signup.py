from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import askyesno
from mysql.connector import *


class Signup:
    def __init__(self):
        root1 = Tk()
        root1.title("Signup")
        root1.geometry("750x550")
        root1.configure(background="light blue")
        label = Label(root1, text="Fill Your Details", font=("times new roman", 30, "bold"), bg="light blue",
                      fg="black")
        label.place(x=230, y=10)
        label1 = Label(root1, text="Name:", font=("times new roman", 13, "bold"), bg="light blue", fg="black")
        label1.place(x=20, y=100)
        textbox1 = Entry(root1, width=25, font=("times new roman", 10, "bold"))
        textbox1.place(x=80, y=103)
        label2 = Label(root1, text="Email:", font=("times new roman", 13, "bold"), bg="light blue", fg="black")
        label2.place(x=370, y=100)
        textbox2 = Entry(root1, width=25, font=("times new roman", 10, "bold"))
        textbox2.place(x=430, y=103)
        label3 = Label(root1, text="Phone Number:", font=("times new roman", 13, "bold"), bg="light blue", fg="black")
        label3.place(x=20, y=170)
        textbox3 = Entry(root1, width=25, font=("times new roman", 10, "bold"))
        textbox3.place(x=150, y=176)
        username = StringVar()
        password = StringVar()
        label4 = Label(root1, text="Username:", font=("times new roman", 13, "bold"), bg="light blue", fg="black")
        label4.place(x=370, y=170)
        textbox4 = Entry(root1, width=25, font=("times new roman", 10, "bold"), textvariable=username)
        textbox4.place(x=460, y=176)
        label5 = Label(root1, text="Password:", font=("times new roman", 13, "bold"), bg="light blue", fg="black")
        label5.place(x=20, y=240)
        textbox5 = Entry(root1, width=25, font=("times new roman", 10, "bold"), show="*", textvariable=password)
        textbox5.place(x=110, y=245)
        label6 = Label(root1, text="Confirm Password:", font=("times new roman", 13, "bold"), bg="light blue",
                       fg="black")
        label6.place(x=320, y=240)
        textbox6 = Entry(root1, width=25, font=("times new roman", 10, "bold"), show="*")
        textbox6.place(x=475, y=245)
        label7 = Label(root1, text="Address:", font=("times new roman", 13, "bold"), bg="light blue", fg="black")
        label7.place(x=20, y=312)
        textbox7 = Entry(root1, font=("times new roman", 10, "bold"))
        textbox7.place(x=110, y=315, height=90, width=400)

        def back():
            root1.destroy()
            import login
            login.Login(user_name="", password1="")

        def sign_up():
            try:
                con = connect(host="localhost", user="root", password="", database="python_mini_project")
                cur = con.cursor()
                query = "insert into users(name,email,ph_no,username,passw,address)values(%s,%s,%s,%s,%s,%s)"
                data = (
                    textbox1.get(), textbox2.get(), textbox3.get(), textbox4.get(), textbox5.get(), textbox7.get())
                cur.execute(query, data)

                if textbox5.get() == textbox6.get() and textbox5.get() != "" and textbox6.get() != "" and textbox1.get() != "" and textbox2.get() != "" and textbox3.get() != "" and textbox4.get() != "" and textbox7.get() != "" and '@gmail.com' in textbox2.get():
                    messagebox.showinfo("Success", "Account Created Successfully")
                    root1.destroy()
                    import login
                    login.Login(user_name=username, password1=password)
                else:
                    messagebox.showerror("Error", "Please fill all the details correctly")
            except Exception as e:
                print(e)

        def Quit():
            ans = askyesno("Quit", "Do you want to quit?")
            if ans:
                root1.destroy()
            else:
                pass

        button1 = Button(root1, text="Signup", font=("times new roman", 15, "bold"), bg="light blue", fg="black",
                         command=sign_up)
        button1.place(x=200, y=450)
        button2 = Button(root1, text="Back", font=("times new roman", 15, "bold"), bg="light blue", fg="black",
                         command=back)
        button2.place(x=300, y=450)
        button3 = Button(root1, text="Cancel", font=("times new roman", 15, "bold"), bg="light blue", fg="black",
                         command=Quit)
        button3.place(x=400, y=450)
        root1.mainloop()


if __name__ == "__main__":
    Signup()
