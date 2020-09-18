import sqlite3
from geolocation import geo_location
from Book_Ride import Ride
from Check_history import checking_history
import geopy
import requests
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.distance import great_circle


class Login_support:
    def support(self,i,ch):
            print("Enter your preference:-  ")
            print("1.update Location")
            print("2.update Availability")
            print("3.Exit")
            i2=int(input("Enter your preference:-  "))
            ch=i2
            if ch==3:
                print("Terminated Successfully")
            if ch==2:
                avail_inp=int(input("Enter 1 if you are available or Enter 0 if you are not available"))
                con2=sqlite3.connect('cab_signup.db')
                c2=con2.cursor()
                c2.execute("UPDATE cab_signup set avail=? where email=?",(avail_inp,i[1]))
                con2.commit()
                con2.close()
                self.support(i,ch)
            elif ch==1:
                in2=input("Press 1 for fetching pickup Location Automatically or Press 2 for Adding Pickup Location Manually:-   ")
                if(in2=="1"):
                    ob1=geo_location()
                    res1=ob1.rider_current_location()
                    print(res1)
                    con2=sqlite3.connect('cab_signup.db')
                    c2=con2.cursor()
                    c2.execute("UPDATE cab_signup set lat=? where email=?",(res1[0],i[1]))
                    c2.execute("UPDATE cab_signup set long=? where email=?",(res1[1],i[1]))
                    con2.commit()
                    con2.close()
                                        
                elif (in2=="2"):
                   
                    ob1=geo_location()
                    arr1=ob1.checking()
                    con2=sqlite3.connect('cab_signup.db')
                    c2=con2.cursor()
                    c2.execute("UPDATE cab_signup set lat=? where email=?",(arr1[1],i[1]))
                    c2.execute("UPDATE cab_signup set long=? where email=?",(arr1[2],i[1]))
                    con2.commit()
                    con2.close()  
                
                self.support(i,ch)
                            