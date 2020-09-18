
from Book_Ride import Ride
from Check_history import checking_history



class options:
    def select(self,i,c):
        print("Please Select your Choice:")
        print("1.Book a Ride")
        print("2.Check History of Rides")
        print("3.Exit")
        temp=Ride()
        inp2=int(input("Enter your Choice:- "))
        c=inp2
        if(c==3):
            print("Disconnected Successfully")
        if(c==1):
            ob1=Ride()
            ob1.booking_ride(i)
            self.select(i,c)
        elif (c==2):
            ob2=checking_history()
            ob2.check(i)
            self.select(i,c)
