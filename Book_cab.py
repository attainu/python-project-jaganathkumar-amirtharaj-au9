import sqlite3
import math
# from Check_history import checking_history
class Booking:	
    def getCab(self,lat,lon,ar):
        with sqlite3.connect("cab_signup.db") as db:
            cursor=db.cursor()
        usr=("SELECT * FROM cab_signup")
        cursor.execute(usr)
        result=cursor.fetchall()
        arr=[]
        arr_details=[]
        if result is not None:
            for i in result: 
                n_lat,n_long=float(i[6]),float(i[7])
                res=(math.sqrt(pow(2,(lat-n_lat))+(pow(2,(lon-n_long)))))
                if(int(i[5]))==1:
                    arr.append(res)
                    arr_details.append([i])
        arr2,arr3=[],[]
        for j in range(0,len(arr)):
            if(arr[j]<3)  :
                arr2.append(arr[j])
                arr3.append(arr_details[j])
            else:
                print("No CAb is Available right Now, please check later")
        # print("there are ",len(arr2),"cabs available Near your locations, please pick a cab from the following")
        for i in range(0,len(arr2)):
            if arr2 is not None:
                
                print(arr3[i][0])
                print("cab Details:-",   "Driver Email:",arr3[i][0][1],",Mobile No:",arr3[i][0][3],",Vehicle No:",arr3[i][0][4])
                conn=sqlite3.connect('booking_ride.db')
                c=conn.cursor()
                u,e,m,s,d,d_email,d_m,d_v=ar[0],ar[1],ar[2],ar[3],ar[4],arr3[i][0][1],arr3[i][0][3],arr3[i][0][4]
                c.execute("""CREATE TABLE IF NOT EXISTS booking_ride(username text,email text,mobile integer,starting_point text,destination text,driver_email text,driver_mobile_no text,driver_vehicle_no text)""")
                c.execute("""INSERT INTO booking_ride (username,email,mobile,starting_point,destination,driver_email,driver_mobile_no,driver_vehicle_no) VALUES (?,?,?,?,?,?,?,?)""",(u,e,m,s,d,d_email,d_m,d_v))
                conn.commit()
                conn.close()
                
                print("cab is Booked ")
                print("1:End Ride")
                # print("2.view History")
                # print("3.Quit")
                end_ride=input("Enter your preference :    ")
                
                if end_ride=="1":
                    print("your ride is ended")
                    break
                else:
                    break
                
                    # print("please enter your preference:")
                    # print("2.view History")
                    # print("3.Quit")
                #     end=input("Enter 1 to end ride or q to Quit :    ")
                #     if(end=="2"):
                #         ob2=checking_history()
                #         ob2.check(i)
                #     elif(end=="3"):
                #         print("terminated Successfully")
                # if(end=="2"):
                #         ob2=checking_history()
                #         ob2.check(i)
                # elif(end_ride=="3"):
                #     print("terminated Successfully")




                
            

       
# if __name__ == '__main__':
#     ob=Booking()
#     print(ob.getCab(13.0878,80.2785))
# "SELECT *, SQRT(POW(2,({}-lat)) + POW(2,({}-lon))) as distance from cab_signup where isavailable = 1 having distance < 3 order by distance limit 1".format(lat,lon)