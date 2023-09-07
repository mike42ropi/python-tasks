# TASK 2: Using Python or PHP or Java or Ruby or JavaScript
# Prompt the user for a number either on a form input or the terminal. 
# Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
# Once you learn functions,revisit this and write this code inside a function.
# Extras:
# If the number is a multiple of 4, print out “divisible by 4”.
# Once you learn functions,revisit this and write this code inside a function.


num= int(input("Enter number: "))
status=0

def divisible(num,status):
    if num%4==0:
        status=(f"{num} Even  and divisible by 4")
    elif num%2==0 and num%4!=0:
        status=(f"{num} Even")
    else:
        status=(f"{num} Odd and not divisible by 4")
    return status

result=divisible(num,status)
print(result)
