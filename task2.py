# TASK 2: Using Python or PHP or Java or Ruby or JavaScript
# Prompt the user for a number either on a form input or the terminal. 
# Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
# Once you learn functions,revisit this and write this code inside a function.
# Extras:
# If the number is a multiple of 4, print out “divisible by 4”.
# Once you learn functions,revisit this and write this code inside a function.

num= int(input("Enter number: "))



if num%2==0 and num%4!=0:
    print("Even")
elif num%4==0:
    print("Even  and divisible by 4")
else:
    print("Odd and not divisible by 4")

