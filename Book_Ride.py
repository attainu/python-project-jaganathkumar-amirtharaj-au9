from geolocation import geo_location
import geopy
import requests
from Book_cab import Booking
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.distance import great_circle
import sqlite3
class Ride:
    def booking_ride(self,i):
        print("connected")
        inp1=int(input("Press 1 for fetching pickup Location Automatically or Press 2 for Adding Pickup Location Manually:-   "))
        ob1=geo_location()
        
        if(inp1==1):
            
            res1=ob1.rider_current_location()
            print(res1)
            out1=ob1.destination(res1[0],res1[1])
            ar=[i[0],i[1],i[3],res1[2],out1[0]]
           
            get2=Booking()
            get2.getCab(float(res1[0]),float(res1[1]),ar)
            
        elif(inp1==2):
            
            arr1=ob1.checking()
            print(arr1)
            l,lo=arr1[1],arr1[2]
            
            out1=ob1.destination(l,lo)
            print(out1)
            ar2=[i[0],i[1],i[3],arr1[0],out1[0]]
            get2=Booking()
            get2.getCab(float(l),float(lo),ar2)
            
           
        

# if __name__ == '__main__':
#     temp=Ride()
#     temp.booking_ride("jagan",)
    

    
            
           
