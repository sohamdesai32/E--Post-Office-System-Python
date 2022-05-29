from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import askyesno
from mysql.connector import *
from datetime import timedelta, date


class TrackPackage:
    def __init__(self, user_name):
        self.user_name = user_name
        track = Tk()
        track.title("Track Package")
        track.geometry("500x600")
        track.configure(background='cyan')
        try:
            conn = connect(host='localhost', user='root', passwd='', database='python_mini_project')
            cursor = conn.cursor()
            cursor.execute("select * from packages where sender_name = '" + user_name + "'")
            rows = cursor.fetchall()
            for row in rows:
                id1 = row[0]
                sender_name = row[4]
                package_type = row[5]
                package_weight = row[7]

                id_label = Label(track, text=f"Package ID : {id1}", font=("Arial", 15, "bold"), bg='cyan')
                id_label.place(x=150, y=10)
                sender_label = Label(track, text=f"Sender Name : {sender_name}", font=("Arial", 15, "bold"), bg='cyan')
                sender_label.place(x=150, y=50)
                package_type = Label(track, text=f"Package Type : {package_type}", font=("Arial", 15, "bold"), bg='cyan')
                package_type.place(x=150, y=90)
                package_weight = Label(track, text=f"Package Weight : {package_weight} kgs", font=("Arial", 15, "bold"),
                                       bg='cyan')
                package_weight.place(x=150, y=130)

            cursor.execute("select * from payment where user_name = '" + user_name + "'")
            rows1 = cursor.fetchall()
            for dist in rows1:
                total_distance = dist[3]
                total_distance_label = Label(track, text=f"Total Distance : {total_distance} kms",
                                             font=("Arial", 15, "bold"), bg='cyan')
                total_distance_label.place(x=150, y=170)
                if total_distance <= 200:
                    Date_req = date.today() + timedelta(days=3)
                    arrival = Label(track, text=f"Arrival Date : {Date_req}", font=("Arial", 15, "bold"), bg='cyan')
                    arrival.place(x=150, y=210)
                elif 201 < total_distance <= 400:
                    Date_req = date.today() + timedelta(days=7)
                    arrival = Label(track, text=f"Arrival Date : {Date_req}", font=("Arial", 15, "bold"), bg='cyan')
                    arrival.place(x=150, y=210)
                elif 401 < total_distance <= 800:
                    Date_req = date.today() + timedelta(days=12)
                    arrival = Label(track, text=f"Arrival Date : {Date_req}", font=("Arial", 15, "bold"), bg='cyan')
                    arrival.place(x=150, y=210)
                elif total_distance > 800:
                    Date_req = date.today() + timedelta(days=15)
                    arrival = Label(track, text=f"Arrival Date : {Date_req}", font=("Arial", 15, "bold"), bg='cyan')
                    arrival.place(x=150, y=210)


        except Exception as e:
            print(e)
        track.mainloop()


if __name__ == '__main__':
    TrackPackage("")
