from tkinter import *
from tkinter import messagebox
from geopy.distance import distance
from geopy.geocoders import Nominatim
from mysql.connector import *


class Admin:
    def __init__(self, user_name):
        self.user_name = user_name

        admin_window = Tk()
        admin_window.title("Admin")
        admin_window.geometry("600x650+500+100")
        admin_window.resizable(0, 0)
        menu = Menu(admin_window)
        admin_window.config(menu=menu)
        account = Menu(menu, tearoff=0)
        photo = PhotoImage(file="admin.png")
        photo_label = Label(admin_window, image=photo)
        photo_label.place(x=0, y=0)

        def open_login():
            from tkinter.messagebox import askyesno
            ans = askyesno("Quit", "Do you want to quit?")
            if ans:
                admin_window.destroy()
            else:
                pass
            import login
            login.Login()

        def open_add_user():
            admin_window.destroy()
            import view_user
            view_user.View()

        def open_add_packages():
            admin_window.destroy()
            import view_packages
            view_packages.ViewPackages()

        menu.add_cascade(label="Accounts", menu=account)
        account.add_command(label="View Account", command=open_add_user)
        package = Menu(menu, tearoff=0)
        menu.add_cascade(label="Packages", menu=package)
        package.add_command(label="View Packages", command=open_add_packages)
        logout = Menu(menu, tearoff=0)
        menu.add_cascade(label="Logout", menu=logout)
        logout.add_command(label="Logout",command=open_login)

        admin_window.mainloop()


if __name__ == '__main__':
    Admin("admin")
