import sqlite3
from geolocation import geo_location
from Book_Ride import Ride
from Check_history import checking_history
from support_login import Login_support
from rider_options import options
import geopy
import requests
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.distance import great_circle

class USER_LOGIN:
    def cab_login(self):

        while True:
            e=input("Enter the Email Address:-  ")
            p=input("Enter the Password:-   ")
            with sqlite3.connect("cab_signup.db") as db:
                cursor=db.cursor()
            usr=("SELECT * FROM cab_signup WHERE email=? AND pass=?")
            cursor.execute(usr,[(e),(p)])
            result=cursor.fetchall()
            if result:
                for i in result:                     
                    support_log=Login_support()
                    support_log.support(i,0)
                break
            
            else:
                print("Email or password is not recoganized")
    

    def rider_login(self):
        while True:
            e=input("Enter the Email Address:-  ")
            p=input("Enter the Password:-   ")
            with sqlite3.connect("rider_signup.db") as db:
                cursor=db.cursor()
            usr=("SELECT * FROM rider_signup WHERE email=? AND pass=?")
            cursor.execute(usr,[(e),(p)])
            result=cursor.fetchall()
            if result:
                for i in result:
                    
                    print("Connected")
                    print("Welcome")
                    ride_option=options()
                    ride_option.select(i,0)
                    
                break
            else:
                print("Email or password is not recoganized")
