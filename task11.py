# TASK 11: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes the date of birth of a person and the program outputs the age in 
# terms of years,months,days TODAY.

from datetime import datetime

today= datetime.now()
dob=input("Enter Date of birth(dd-mm-yyyy): ")
sdob = dob.split("-")

if len(sdob)!=3 or int(sdob[0])>31 \
   or int(sdob[1])>12 or int(sdob[2])<1900\
   or int(sdob[2])>2023:
    print("Wrong date fomart")
else:
    y=today.year - int(sdob[-1])
    m= today.month -int(sdob[-2])
    d= today.day-int(sdob[-3])
    if d<0:
        m=m-1
        d=d+31
    else:
        pass
    if m<0:
        y=y-1
        m=m+12
    else:
        pass
    
    
    age= str(y)+"-"+str(m)+"-"+str(d)
    print(age)   

