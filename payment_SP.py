import random
from tkinter import *
from tkinter import messagebox

from geopy.distance import distance
from geopy.geocoders import Nominatim
from mysql.connector import *


class PaymentSP:
    def __init__(self, user_name):
        self.user_name = user_name

        payment_window1 = Tk()
        payment_window1.title("Payment")
        payment_window1.geometry("350x600+500+100")
        payment_window1.configure(background='cyan')
        label = Label(payment_window1, text="Payment Details", font=("Helvetica", 20), bg='cyan', fg='white')
        label.pack(fill=X)

        postal_charges = 200
        postal_charges_label = Label(payment_window1, text="Postal Charges:  200", font=("Helvetica", 15), bg='cyan',
                                     fg='white')
        postal_charges_label.place(x=10, y=50)
        try:
            conn = connect(host='localhost', database='python_mini_project', user='root', password='')
            cursor = conn.cursor()
            cursor.execute("select * from packagesSP where user_name = '" + user_name + "'")
            row = cursor.fetchall()
            for i in row:
                weight = i[5]

                geo = Nominatim(user_agent="myGeocoder")
                c = geo.geocode("Mumbai")
                d = geo.geocode("Pune")
                f = (c.longitude, c.latitude)
                g = (d.longitude, d.latitude)
                distance_in_km = distance(f, g).km
                if distance_in_km <= 50 and weight == "0-1 kg":
                    dist_cost = 20
                elif distance_in_km <= 50 and weight == "1-2 kgs":
                    dist_cost = 30
                elif 51 <= distance_in_km <= 200 and weight == "1-2 kgs":
                    dist_cost = 70
                elif 201 <= distance_in_km <= 1000 and weight == "1-2 kgs":
                    dist_cost = 120
                elif 1000 <= distance_in_km <= 2000 and weight == "1-2 kgs":
                    dist_cost = 170
                elif distance_in_km > 2000 and weight == "1-2 kgs":
                    dist_cost = 250

                elif distance_in_km <= 50 and weight == "2-3 kgs":
                    dist_cost = 110
                elif 51 <= distance_in_km <= 200 and weight == "2-3 kgs":
                    dist_cost = 170
                elif 201 <= distance_in_km <= 1000 and weight == "2-3 kgs":
                    dist_cost = 300
                elif 1000 <= distance_in_km <= 2000 and weight == "2-3 kgs":
                    dist_cost = 350
                elif distance_in_km > 2000 and weight == "2-3 kgs":
                    dist_cost = 385

                elif distance_in_km <= 50 and weight == "3-4 kgs":
                    dist_cost = 140
                elif 51 <= distance_in_km <= 200 and weight == "3-4 kgs":
                    dist_cost = 200
                elif 201 <= distance_in_km <= 1000 and weight == "3-4 kgs":
                    dist_cost = 360
                elif 1000 <= distance_in_km <= 2000 and weight == "3-4 kgs":
                    dist_cost = 385
                elif distance_in_km > 2000 and weight == "3-4 kgs":
                    dist_cost = 460
                elif distance_in_km <= 50 and weight == "4-5 kgs":
                    dist_cost = 160
                elif 51 <= distance_in_km <= 200 and weight == "4-5 kgs":
                    dist_cost = 220
                elif 201 <= distance_in_km <= 1000 and weight == "4-5 kgs":
                    dist_cost = 380
                elif 1000 <= distance_in_km <= 2000 and weight == "4-5 kgs":
                    dist_cost = 420
                elif distance_in_km > 2000 and weight == "4-5 kgs":
                    dist_cost = 500
                else:
                    dist_cost = 60

                gst = (0.18 * postal_charges) + (0.18 * dist_cost)
                total_dist = Label(payment_window1, text=f"Total Distance:  %.2f km" % distance_in_km,
                                   font=("Helvetica", 15),
                                   bg='cyan', fg='white')
                total_dist.place(x=10, y=100)

                total_dist_cost = Label(payment_window1, text=f"Total Distance Cost:   {dist_cost}",
                                        font=("Helvetica", 15),
                                        bg='cyan', fg='white')
                total_dist_cost.place(x=10, y=150)

                gst_label = Label(payment_window1, text=f"GST:   {gst}", font=("Helvetica", 15), bg='cyan',
                                  fg='white')
                gst_label.place(x=10, y=200)
                total_cost = postal_charges + dist_cost + gst
                total_cost = Label(payment_window1, text=f"Total Cost:   {total_cost}",
                                   font=("Helvetica", 15), bg='cyan', fg='white')
                total_cost.place(x=10, y=250)
        except Exception as e:
            print(e)

        def Next():
            payment_window1.destroy()
            import recieptSP
            recieptSP.RecieptSP(user_name=user_name)

        proceed = Button(payment_window1, text="Proceed", font=("Helvetica", 15), bg='cyan', fg='white')
        proceed.place(x=10, y=300)
        proceed.bind("<Button-1>", Next)

        back = Button(payment_window1, text="Back", font=("Helvetica", 15), bg='cyan', fg='white')

        payment_window1.mainloop()


if __name__ == "__main__":
    PaymentSP("sachin")
