import sqlite3
from geolocation import geo_location
from login import USER_LOGIN
class USER_SIGNUP:
    def cabsignup(self):
        u2=input("Enter the Username:-   ")
        e2=input("Enter the Email Address:-  ")
        p2=input("Enter the Password:-   ")
        m2=int(input("Enter the Mobile Number:-  "))
        v2=(input("Enter the Vehicle Number:- "))
        a2=(int(input("if you are available enter 1 or enter 0:-    ")))
        geo_obj=geo_location()
        res1=geo_obj.rider_current_location()
        lat,lo=str(res1[0]),str(res1[1])

        con2=sqlite3.connect('cab_signup.db')
        c2=con2.cursor()
        c2.execute("""CREATE TABLE IF NOT EXISTS cab_signup(username text,email text,pass password,mobile integer,cab_no text,avail integer,lat text,long text)""")
        c2.execute("""INSERT INTO cab_signup (username,email,pass,mobile,cab_no,avail,lat,long)VALUES (?,?,?,?,?,?,?,?)""",(u2,e2,p2,m2,v2,a2,lat,lo))
        con2.commit()
        con2.close()
        print("Successfully Saved Data to DB")
        usr_l=USER_LOGIN()
        usr_inp=input("To LOGIN press 1/ To QUIT press q:-   ")
        if(usr_inp.lower()=="1"):
            l_inp=input("CAB/RIDER:-    ")
            if(l_inp.lower()=="cab"):
                usr_l.cab_login()     
            elif (l_inp.lower()=="rider"):
                usr_l.rider_login()
            else:
                print("Please enter either CAB or RIDER")
        elif(usr_inp.lower()=="q"):
             print("Disconnected Successfully")
        
    def ridersignup(self):
        u1=input("Enter the Username:-   ")
        e1=input("Enter the Email Address:-  ")
        p1=input("Enter the Password:-   ")
        m1=int(input("Enter the Mobile Number:-  "))
        con=sqlite3.connect('rider_signup.db')
        c=con.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS rider_signup(username text,email text,pass text,mobile integer)""")
        c.execute("""INSERT INTO rider_signup (username,email,pass,mobile) VALUES (?,?,?,?)""",(u1,e1,p1,m1))
        con.commit()
        con.close()
        print("Successfully Saved Data to DB")
        usr_l2=USER_LOGIN()
        usr_inp=input("To LOGIN press 1 or  To QUIT press q:-   ")
        if(usr_inp.lower()=="1"):
            l_inp=input("CAB/RIDER:-    ")
            if(l_inp.lower()=="cab"):
                usr_l2.cab_login()     
            elif (l_inp.lower()=="rider"):
                usr_l2.rider_login()
            else:
                print("Please enter either CAB or RIDER")
        elif(usr_inp.lower()=="q"):
             print("Disconnected Successfully")
        
        

        

        
 # ('{}','{}','{}',{})".format(self.r_u,self.r_e,self.r_p,self.r_m))
        # :username,:email,:pass,:mobile)",{'username':self.r_u,'email':self.r_e,'pass':self.r_p,'mobile':r_m
# ('{}','{}','{}',{},'{}')".format(self.u,self.e,self.p,self.m,self.c))
        # :username,:email,:pass,:mobile,:cab_no)",{'username':self.u,'email':self.e,'pass':self.p,'mobile':self.m,'cab_no':self.c}