import geopy
import requests
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.distance import great_circle

class geo_location:
    def rider_current_location(self):
        res=requests.get("https://ipinfo.io/")
        data=res.json()
        curr_loc=data['loc'].split(',')
        curr_lat=(curr_loc[0])
        curr_long=(curr_loc[1])
        city=data['city']
        state=data['region']
        return([curr_lat,curr_long,city,state])
    def checking(self):
        geolocator = Nominatim(user_agent="cab_booking_project")
        ma=input("Enter your location:- ") 
        location = geolocator.geocode(ma)
        print(location)
        return([ma,location.latitude,location.longitude])
         
    def destination(self,l,lo):
        geolocator = Nominatim(user_agent="cab_booking_project")
        # location = geolocator.reverse(curr)
        # location = geolocator.geocode("coimbatore")
        # print(location.address)
        des=input("Enter the Destination:-  ")
        location2 = geolocator.geocode(des)
        loc2=(location2.latitude,location2.longitude)
        loc1=(l,lo)
        # print(loc1,loc2)
        # print(int(geodesic(loc1,loc2).km))
        # print(int(great_circle(loc1,loc2).km))
        return ([des,loc1,loc2,(int(great_circle(loc1,loc2).km))])

        
# if __name__ == '__main__':
#     obj=geo_location()
#     print(obj.manual_entry())
    # arr1=obj.rider_current_location()
    # print(arr1)
    # geolocator = Nominatim(user_agent="cab_booking_project")
    # To find the current address use the below code
    # lat_long=(str(arr1[0]),str(arr1[1]))
    
    # location = geolocator.reverse(lat_long)
    # out=obj.destination(arr1[0],arr1[1])
    # print(out)
    