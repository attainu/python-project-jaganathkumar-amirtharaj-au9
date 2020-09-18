import sqlite3
from geolocation import geo_location
from Book_Ride import Ride
class checking_history:
    def check(self,i):
        print("connected")
        e=i[1]
        with sqlite3.connect("booking_ride.db") as db:
            cursor=db.cursor()
        usr=("SELECT * FROM booking_ride WHERE email=?")
        cursor.execute(usr,[(e)])
        print(cursor.fetchall())
       
