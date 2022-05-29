from tkinter import *
from tkinter import messagebox, ttk
from geopy.distance import distance
from geopy.geocoders import Nominatim
from mysql.connector import *


class ViewPackages:
    def __init__(self):
        view = Tk()
        view.title("View User")
        view.geometry("1900x600")
        view.configure(background='#00BFFF')
        cols = ("ID", " Receiver Name", "Email", "Phone", "Sender name", "Package Type", "Weight")
        tree = ttk.Treeview(view, columns=cols, show="headings")

        def show():
            try:
                for col in cols:
                    tree.heading(col, text=col)
                    tree.grid(row=1, column=0, columnspan=1, padx=10, pady=10)
                conn = connect(host="localhost", user="root", password="", database="python_mini_project")
                cursor = conn.cursor()
                cursor.execute("SELECT id,reciever_name,reciever_email,reciever_ph_no,sender_name,package_type,package_weight FROM packages")
                rows = cursor.fetchall()
                for i in rows:
                    tree.insert('', 'end', values=i)
                cursor.execute("SELECT total_cost FROM payment")
                rows = cursor.fetchall()
                for i in rows:
                    tree.insert('', 'end', values=i)

            except Error as e:
                print(e)

        name1 = Label(view, text="Name", font=("arial", 10, "bold"), bg="#00BFFF", fg="white")
        name1.place(x=350, y=300)
        name_entry = Entry(view, width=20)
        name_entry.place(x=470, y=300)

        email1 = Label(view, text="Email",font=("arial", 10, "bold"), bg="#00BFFF", fg="white")
        email1.place(x=700, y=300)
        email_entry = Entry(view, width=20)
        email_entry.place(x=800, y=300)

        phone1 = Label(view, text="Phone", font=("arial", 10, "bold"), bg="#00BFFF", fg="white")
        phone1.place(x=350, y=350)
        phone_entry = Entry(view, width=20)
        phone_entry.place(x=470, y=350)

        username1 = Label(view, text="Username",font=("arial", 10, "bold"), bg="#00BFFF", fg="white")
        username1.place(x=700, y=350)
        username_entry = Entry(view, width=20)
        username_entry.place(x=800, y=350)

        address1 = Label(view, text="Address", font=("arial", 10, "bold"), bg="#00BFFF", fg="white")
        address1.place(x=350, y=400)
        address_entry = Entry(view, width=20)
        address_entry.place(x=470, y=400)

        id1 = Label(view, text="ID", font=("arial", 10, "bold"), bg="#00BFFF", fg="white")
        id1.place(x=700, y=400)
        id_entry = Entry(view, width=20)
        id_entry.place(x=800, y=400)

        def update():
            if id_entry.get() == "":
                messagebox.showinfo("Error", "Please enter ID")
            else:
                tree.grid_forget()
                for i in tree.get_children():
                    tree.delete(i)
                try:

                    conn = connect(host="localhost", user="root", password="", database="python_mini_project")
                    cursor = conn.cursor()
                    data = (name_entry.get(), email_entry.get(), phone_entry.get(), username_entry.get(),
                            address_entry.get(), id_entry.get())
                    cursor.execute("update packages set reciever_name=%s, reciever_email=%s, reciever_ph_no=%s, sender_name=%s, address=%s where id=%s", data)

                except Exception as e:
                    print(e)

        def delete():
            if id_entry.get() == "":
                messagebox.showinfo("Error", "Please enter ID")
            else:
                tree.grid_forget()
                for i in tree.get_children():
                    tree.delete(i)
                try:
                    conn = connect(host="localhost", user="root", password="", database="python_mini_project")
                    cursor = conn.cursor()
                    data = [id_entry.get()]
                    cursor.execute("delete from packages where id=%s", data)
                    for row in tree.grid_slaves():
                        tree.grid_forget()
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

        back = Button(view, text="Back", font=("arial", 10, "bold"), bg="#00BFFF", command=back)
        back.place(x=450, y=550)

        view.mainloop()


if __name__ == "__main__":
    ViewPackages()
