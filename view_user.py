from tkinter import *
from tkinter import messagebox, ttk
from geopy.distance import distance
from geopy.geocoders import Nominatim
from mysql.connector import *


class View:
    def __init__(self):
        view = Tk()
        view.title("View User")
        view.geometry("1900x600")
        view.configure(background='cyan')
        cols = ("ID", "Name", "Email", "Phone", "Username", "Address")
        tree = ttk.Treeview(view, columns=cols, show="headings")

        def show():
            try:
                for col in cols:
                    tree.heading(col, text=col)
                    tree.grid(row=1, column=0, columnspan=2, padx=10, pady=20)
                conn = connect(host="localhost", user="root", password="", database="python_mini_project")
                cursor = conn.cursor()
                cursor.execute("SELECT id,name,email,ph_no,username,address FROM users")
                rows = cursor.fetchall()
                for i in rows:
                    tree.insert('', 'end', values=i)

            except Error as e:
                print(e)

        name1 = Label(view, text="Name", font=("bold", 10), bg="cyan", fg="black")
        name1.place(x=350, y=300)
        name_entry = Entry(view, width=20)
        name_entry.place(x=470, y=300)

        email1 = Label(view, text="Email", font=("bold", 10), bg="cyan", fg="black")
        email1.place(x=700, y=300)
        email_entry = Entry(view, width=20)
        email_entry.place(x=800, y=300)

        phone1 = Label(view, text="Phone", font=("bold", 10), bg="cyan", fg="black")
        phone1.place(x=350, y=350)
        phone_entry = Entry(view, width=20)
        phone_entry.place(x=470, y=350)

        username1 = Label(view, text="Username", font=("bold", 10), bg="cyan", fg="black")
        username1.place(x=700, y=350)
        username_entry = Entry(view, width=20)
        username_entry.place(x=800, y=350)

        address1 = Label(view, text="Address", font=("bold", 10), bg="cyan", fg="black")
        address1.place(x=350, y=400)
        address_entry = Entry(view, width=20)
        address_entry.place(x=470, y=400)

        id1 = Label(view, text="ID", font=("bold", 10), bg="cyan", fg="black")
        id1.place(x=700, y=400)
        id_entry = Entry(view, width=20)
        id_entry.place(x=800, y=400)

        def update():
            if id_entry.get() == "":
                messagebox.showinfo("Error", "Please enter ID")
            else:
                tree.grid_forget()
                for item in tree.get_children():
                    tree.delete(item)
                try:
                    conn = connect(host="localhost", user="root", password="", database="python_mini_project")
                    cursor = conn.cursor()
                    data = (name_entry.get(), email_entry.get(), phone_entry.get(), username_entry.get(),
                            address_entry.get(), id_entry.get())
                    cursor.execute("update users set name=%s, email=%s, ph_no=%s, username=%s, address=%s where id=%s",
                                   data)
                    messagebox.showinfo("Success", "User Updated Successfully")

                except Exception as e:
                    print(e)

        def delete():
            if id_entry.get() == "":
                messagebox.showinfo("Error", "Please enter ID")
            else:
                tree.grid_forget()
                for item in tree.get_children():
                    tree.delete(item)
                try:
                    conn = connect(host="localhost", user="root", password="", database="python_mini_project")
                    cursor = conn.cursor()
                    data = [id_entry.get()]
                    cursor.execute("delete from users where id=%s", data)
                    for row in tree.grid_slaves():
                        tree.grid_forget()
                    messagebox.showinfo("Success", "User Deleted Successfully")
                except Exception as e:
                    print(e)

        show1 = Button(view, text="Show", command=show)
        show1.place(x=350, y=250)
        update1 = Button(view, text="Update", command=update)
        update1.place(x=500, y=250)
        delete1 = Button(view, text="Delete", command=delete)
        delete1.place(x=650, y=250)

        def back():
            view.destroy()
            import admin
            admin.Admin("admin")

        back = Button(view, text="Back", font=("arial", 10, "bold"), bg="cyan", command=back)
        back.place(x=900, y=550)

        view.mainloop()


if __name__ == "__main__":
    View()
