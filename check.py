import sqlite3

from login import USER_LOGIN
from signup import USER_SIGNUP

class verify:
    def checking(self):
        obj1=USER_SIGNUP()
        obj2=USER_LOGIN()
        inp=input("LOGIN/SIGNUP:-   ")
        if(inp.lower()=="login"):
            l_inp=input("CAB/RIDER:-    ")
            if(l_inp.lower()=="cab"):
                obj2.cab_login()     
            elif (l_inp.lower()=="rider"):
                obj2.rider_login()
            else:
                print("Please enter either CAB or RIDER")
        elif(inp.lower()=="signup"):
            s_inp=input("CAB/RIDER:-    ")
            if(s_inp.lower()=="cab"):
                obj1.cabsignup()
            elif (s_inp.lower()=="rider"):
                obj1.ridersignup()
          
            else:
                print("Please enter either CAB or RIDER")