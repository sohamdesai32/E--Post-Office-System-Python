from geopy.distance import geodesic, distance
# from geopy.geocoders import Nominatim
# #
# geo = Nominatim(user_agent="myGeocoder")
# c = geo.geocode("Sumukh Darshan,kandivali")
# d = geo.geocode("powai")
# f = (c.longitude, c.latitude)
# g = (d.longitude, d.latitude)
# a = distance(f, g).km
# print("%.3f" % a)
# from tkinter import Tk, Button
# from tkinter.ttk import Combobox
#
# root = Tk()
# root.title("Distance Calculator")
# root.geometry("300x200")
# q = Combobox(root, width=30, values=["0.5-1", "1-5", "5-10", "10-20"])
# q.pack()
# b = Button(root, text="Calculate", command=lambda: print(q.get()))
# b.pack()
# root.mainloop()
from datetime import timedelta, date

Date_req = date.today() + timedelta(days=15)

print(Date_req)
