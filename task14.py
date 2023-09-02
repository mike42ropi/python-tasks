# TASK 14: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of 2 values and adds them. 
# The program should only accept numbers and floats only or otherwise display an
# error “invalid character entered” and take the user to re-enter the inputs .

while True:
    val1= input("Enter a value: ")
    val2= input("Enter a value: ")

    try:
        num1 = float(val1)
        num2 = float(val2)

        sum = num1  + num2
        print(sum)
        break
    except ValueError:
        print("Invalid character entered")


# sum =0
# i=0
# while i<10:
#     sum=sum+i
#     print(sum)
#     i=i+1