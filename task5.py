# TASK 5: Using Python or PHP or Java or Ruby or JavaScript
# Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables.
# Return the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us

var1 = int(input("Enter number: "))
var2 = int(input("Enter number: "))
var3 = int(input("Enter number: "))

def largest_number(var1,var2,var3):
    status = ""
    if var1>var2 and var1>var3:
        status=("var1 is the largest")
    elif var2>var1 and var2>var3:
        status=("var2 is the largest")
    elif var3>var1 and var3>var2:
        status=("var3 is the largest")
    else:
        status=("They are all same")
    return status
result = largest_number(var1,var2,var3)
print(result)
