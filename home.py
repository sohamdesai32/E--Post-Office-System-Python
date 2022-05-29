from tkinter import *
from tkinter import messagebox
from mysql.connector import *


class Home:
    def __init__(self, user_name):
        self.user_name = user_name

        home = Tk()
        home.title("Home")
        home.geometry("1366x720+0+0")
        photo = PhotoImage(file="home.v1.png")
        photo_label = Label(home, image=photo)
        photo_label.place(x=0, y=0)

        def about_us():
            home.destroy()
            import about
            about.About(user_name)

        def open_login():
            from tkinter.messagebox import askyesno
            ans = askyesno("Quit", "Do you want to quit?")
            if ans:
                home.destroy()
            else:
                pass
            import login
            login.Login()

        def user_info():
            home.destroy()
            import user_info
            username = user_name
            user_info.User_info(user_name=username)

        def send_package():
            home.destroy()
            import send_package
            username = user_name
            send_package.Package(self.user_name)

        def speed_post():
            home.destroy()
            import speed_post
            username = user_name
            speed_post.Package_SP(self.user_name)
        def track():
            home.destroy()
            import track_package
            username = user_name
            track_package.TrackPackage(self.user_name)
        mymenu = Menu(home)
        home.config(menu=mymenu)
        filemenu = Menu(mymenu, tearoff=0)
        mymenu.add_cascade(label="Services", menu=filemenu)
        filemenu.add_command(label="Send a Package", command=send_package)
        filemenu.add_separator()
        filemenu.add_command(label="Speed Post", command=speed_post)
        user = Menu(mymenu, tearoff=0)
        mymenu.add_cascade(label="Account", menu=user)
        user.add_command(label="User Information", command=user_info)
        user.add_separator()
        user.add_command(label="Track Package", command=track)
        aboutmenu = Menu(mymenu, tearoff=0)
        mymenu.add_cascade(label="About", menu=aboutmenu)
        aboutmenu.add_command(label="About us", command=about_us)
        logout = Menu(mymenu, tearoff=0)
        mymenu.add_cascade(label="Logout", menu=logout)
        logout.add_command(label="Logout", command=open_login)

        home.mainloop()


if __name__ == "__main__":
    Home(user_name="falguni")
