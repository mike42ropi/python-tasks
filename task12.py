# TASK 12: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prints the largest of 4 inputs taken in from a user.
# Assume that the user would not enter any two numbers which are the same.
# Once you learn functions,revisit this and write this code inside a function.


i1 =input("Enter number: ")
i2 =input("Enter number: ")
i3 =input("Enter number: ")
i4 =input("Enter number: ")

if i1>i2 and i1>i3:
    print("i1 is the largest")
elif i2>21 and i2>i3:
    print("i2 is the largest")
elif i3>i1 and i3>i2:
    print("i3 is the largest")
else:
    print("i4 is the largest")