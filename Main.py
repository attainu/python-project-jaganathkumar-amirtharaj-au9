from check import verify


if __name__ == '__main__':
    print("****WELCOME TO PYTHON CAB BOOKING PROBLEM PROJECT****")
    inp=input("For Login/Signup Press 1 to Exit press q:-   ")
    if(inp.lower()=="q"):
        print("Disconnected Successfully")
    else:
        obj=verify()
        obj.checking()



#BOOKING A CAB def getCab(self,lat,lon): query = "SELECT *, SQRT(POW(2,({}-lat)) + POW(2,({}-lon))) as distance from cab_booking.driver_info where isavailable = 1 having distance < 3 order by distance limit 1".format(lat,lon) cur = self.con.cursor() cur.execute(query) cabInfo = list(cur) self.con.commit() return cabInfo 
   



    



        


