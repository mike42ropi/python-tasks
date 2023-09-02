# TASK 3: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which gets a phone number from a form input or terminal. 
# Validates the phone number by checking if it starts with +254.. or 07.. or 71… or 254.. or 01... Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”
# Once you learn functions,revisit this and write this code inside a function.

pnum= str(input("Enter number: "))
phone=0

if len(pnum)==10 and (pnum.startswith("07")) or (pnum.startswith("71")) or(pnum.startswith("01")):
    phone="+254" + (pnum[1:])
    print(phone)
elif (len(pnum)==13) and (pnum.startswith("+254")):
    phone="+254" + (pnum[4:])
    print(phone)

elif ((len(pnum)==12)) and (pnum.startswith("254")):
    phone="+254" + (pnum[3:])
    print(phone)
else:
    print("invalid phone number")
