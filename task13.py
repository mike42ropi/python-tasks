# TASK 13: Using Python or PHP or Java or Ruby or JavaScript or C# or Go
# Write a program that takes the email and password as input from a user and checks
# if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print 
# “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3
# tries after which it notifies you that you have been blocked.




max_attempts=4

for attempts in range(1,max_attempts+1):
    password1 = "Admin@123"
    username1 = "admin@mail.com"
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    
    if password==password1 and username==username1:
        print("Access granted")
        break
    if (password!=password1 and username!=username1) and (attempts>0 and attempts<4) :
            rem_attempts=max_attempts-attempts
            print("Incorrect username or password"+" ",rem_attempts)
    elif rem_attempts>0:
            print("blocked")
    else:
        pass
