# TASK 4: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which accepts email as form input or from terminal.
# Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.
# Once you learn functions,revisit this and write this code inside a function.

email= input("Enter email: ")


if (len(email)==0 or email.isupper or "@" not in email or " " in email or "." not in email) or (email.index(".")<=email.index("@")) or  (email.index("@")<0):
    print(email +" "+"is an invalid email")
elif email.endswith(".") or email.count("@")>1:
     print(email +" "+"is an invalid email")
else:
    print(email + " " + " is valid email")