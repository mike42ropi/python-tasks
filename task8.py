# TASK 8: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes as input the speed of a car e.g 80. 
# If the speed is less than 70, it should print “Ok”. Otherwise, 
# for every 5 km/s above the speed limit (70), 
# it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, 
# the function should print: “License suspended”.

speed= float(input("Enter speed: "))
ok_speed = 70
diff_speed=((speed-ok_speed)/5)

if speed == ok_speed:
    print("OK")
else:
    diff_speed=((speed-ok_speed)/5) 
    print("points" , " ", diff_speed) 
    if diff_speed>=12:
        diff_speed=((speed-ok_speed)/5) 
        print("license suspeneded")
        
    else:
        pass