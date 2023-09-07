# TASK 6:Using Python or PHP or Java or Ruby or JavaScript
# Write a program input a password. Give them only 4 attempts to check the passwords 
# entered against “admin@123”. If the password is correct access is granted. 
# After you show them a message , the account is blocked.
# Once you learn functions,revisit this and write this code inside a function.


# passd= input("Enter password: ")

# def my_password(passd):
#     password ="admin@123"
#     total_attempts = 4
#     status = ""
#     for attempts in range(1, total_attempts+1):
#         if (passd==password):
#             status="Access Granted"
#             break
#         if (passd!=password) and (attempts>0 and attempts<4):
#             rem_attempts =total_attempts - attempts
#             status= ("Access denied.Remaining attempts",(rem_attempts))
#         elif attempts==4:
#             status="Account is blocked"
#         else:
#             pass
#     return status
# result =my_password(passd)
# print(result)
passd = input("Enter password: ")

def my_password(passd):
    password = "admin@123"
    total_attempts = 4
    status = ""
    passd = input("Enter password again: ")

    for attempts in range(1, total_attempts + 1):
        if passd == password:
            status = "Access Granted"
            return status
                     
        if attempts < total_attempts and (attempts>0 and attempts<4):
            rem_attempts = total_attempts - attempts
            status = "Access denied. Remaining attempts:", rem_attempts
            
        else:
            status = "Account is blocked"
            return status

result = my_password(passd)
print(result)
