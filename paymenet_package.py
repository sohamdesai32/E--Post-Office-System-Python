import random
from tkinter import *
from tkinter import messagebox
from geopy.distance import distance
from geopy.geocoders import Nominatim
from mysql.connector import *


class Payment:
    def __init__(self, user_name):
        self.user_name = user_name

        payment_window = Tk()
        payment_window.title("Payment")
        payment_window.geometry("350x600+500+100")
        payment_window.configure(background='#00BFFF')
        label = Label(payment_window, text="Payment Details", font=("Helvetica", 20), bg='red', fg='white')
        label.pack(fill=X)
        package_charges = 100
        postage_amt = Label(payment_window, text=f"Postage Amount   :   {package_charges}", font=("Helvetica", 15),
                            bg='#00BFFF')

        postage_amt.place(x=50, y=150)
        try:
            conn = connect(host='localhost', database='python_mini_project', user='root', password='')
            cursor = conn.cursor()
            cursor.execute(f"select * from packages where sender_name='{user_name}'")
            data = cursor.fetchall()
            for row in data:
                weight = row[7]
                current_location = row[8]
                destination = row[9]
                geo = Nominatim(user_agent="myGeocoder")
                c = geo.geocode(current_location)
                d = geo.geocode(destination)
                f = (c.longitude, c.latitude)
                g = (d.longitude, d.latitude)
                distance_in_km = distance(f, g).km

                if distance_in_km <= 50 and weight == "0-0.5":
                    dist_cost = 20
                elif distance_in_km <= 50 and weight == "0.6-2":
                    dist_cost = 30
                elif 51 <= distance_in_km <= 200 and weight == "0.6-2":
                    dist_cost = 70
                elif 201 <= distance_in_km <= 1000 and weight == "0.6-2":
                    dist_cost = 120
                elif 1000 <= distance_in_km <= 2000 and weight == "0.6-2":
                    dist_cost = 170
                elif distance_in_km > 2000 and weight == "0.6-2":
                    dist_cost = 250
                elif distance_in_km <= 50 and weight == "3-6":
                    dist_cost = 110
                elif 51 <= distance_in_km <= 200 and weight == "3-6":
                    dist_cost = 170
                elif 201 <= distance_in_km <= 1000 and weight == "3-6":
                    dist_cost = 300
                elif 1000 <= distance_in_km <= 2000 and weight == "3-6":
                    dist_cost = 350
                elif distance_in_km > 2000 and weight == "3-6":
                    dist_cost = 385

                elif distance_in_km <= 50 and weight == "7-10":
                    dist_cost = 140
                elif 51 <= distance_in_km <= 200 and weight == "7-10":
                    dist_cost = 200
                elif 201 <= distance_in_km <= 1000 and weight == "7-10":
                    dist_cost = 360
                elif 1000 <= distance_in_km <= 2000 and weight == "7-10":
                    dist_cost = 385
                elif distance_in_km > 2000 and weight == "7-10":
                    dist_cost = 460
                else:
                    dist_cost = 60
                a = BooleanVar()
                insureance_amt = 100
                insurance_amt = Label(payment_window, text=f"Insurance Amount : {insureance_amt}",
                                      font=("Helvetica", 15),
                                      bg='#00BFFF')
                gst = (0.18 * package_charges) + (0.18 * dist_cost)
                tot_cost1 = package_charges + dist_cost + gst + 100
                tot_cost = package_charges + dist_cost + gst
                total_cost1 = Label(payment_window,
                                    text=f"Total Cost            :   {tot_cost1}",
                                    font=("Helvetica", 15), bg='#00BFFF')
                total_cost = Label(payment_window,
                                   text=f"Total Cost            :   {tot_cost}",
                                   font=("Helvetica", 15), bg='#00BFFF')
                total_cost.place(x=50, y=420)

                def showIN():
                    if a.get() == 1:
                        total_cost.place_forget()
                        insurance_amt.place(x=50, y=300)

                        total_cost1.place(x=50, y=420)
                    elif a.get() == 0:
                        total_cost1.place_forget()

                        total_cost.place(x=50, y=420)
                        insurance_amt.place_forget()
                    else:
                        pass

                total_dist = Label(payment_window, text=f"Total Distance      :   %.2f km" % distance_in_km,
                                   font=("Helvetica", 15)
                                   , bg='#00BFFF')
                total_dist.place(x=50, y=100)
                dist_charge = Label(payment_window, text=f"Distance Charges  :  {dist_cost}", font=("Helvetica", 15),
                                    bg='#00BFFF')
                dist_charge.place(x=47, y=200)

                gst_amt = Label(payment_window, text=f"GST Amount         :  %.3f" % gst, font=("Helvetica", 15),
                                bg='#00BFFF')
                gst_amt.place(x=47, y=250)
                insurance = Checkbutton(payment_window, text="Do you Want to \n add Insurance?", variable=a, onvalue=1,
                                        offvalue=0, bg='#00BFFF', font=("Helvetica", 10), command=showIN)
                insurance.place(x=50, y=340)
                design = Label(payment_window, text="*" * 50, font=50, bg='#00BFFF')
                design.place(x=3, y=380)
        except Exception as e:
            print(e)

        def receipt():
            try:
                b = random.randint(1, 100)
                conn1 = connect(host='localhost', user='root', password='', database='python_mini_project')
                cur = conn1.cursor()
                data1 = (str(user_name), str(b), str(weight), str(distance_in_km), str(dist_cost), str(gst), tot_cost1,
                         str(package_charges))
                cur.execute("insert into payment values(%s,%s,%s,%s,%s,%s,%s,%s)", data1)
                messagebox.showinfo("Success", "Successful")
                import package_reciept
                package_reciept.Receipt(username=user_name)
                payment_window.destroy()

            except Exception as e:
                print(e)

        button = Button(payment_window, text="Book", font=("Helvetica", 15), bg='#00BFFF', fg="white", command=receipt)
        button.place(x=50, y=500)

        def back():
            payment_window.destroy()
            import send_package
            send_package.Package(user_name=user_name)

        back = Button(payment_window, text="Back", font=("Helvetica", 15), bg='#00BFFF', fg="white", command=back)
        back.place(x=150, y=500)

        payment_window.mainloop()


if __name__ == '__main__':
    Payment("")
