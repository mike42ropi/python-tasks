# TASK 6:Using Python or PHP or Java or Ruby or JavaScript
# Write a program input a password. Give them only 4 attempts to check the passwords 
# entered against “admin@123”. If the password is correct access is granted. 
# After you show them a message , the account is blocked.
# Once you learn functions,revisit this and write this code inside a function.



password ="admin@123"
total_attempts = 4

for attempts in range(1, total_attempts+1):
    passd= input("Enter password: ")
    if (passd==password):
        print("Access Granted")
        break
    if (passd!=password)and (attempts>0 and attempts<4):
        rem_attempts =total_attempts - attempts
        
        print("Access denied.Remaining attempts",(rem_attempts))
        
    elif attempts==4:
        print("Account is blocked")
    else:
        pass