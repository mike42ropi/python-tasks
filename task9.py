# TASK 9: Using Python or PHP or Java or Ruby or JavaScript
# Write a program called stars. It should prompt the user for a number, and 
# it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****.....

num =int(input("Enter number: "))
count = 0
for i in range(1,num+1): 
    print("*"*i)
    count =count+1
    if count==num:
        print(("*"*i)+("."*num))
    
          


    # no =4
    # for j in range(no+1):
    #     print("."*j)



# TASK: Write a program that takes a positive integer as input and prints a pattern of numbers as shown below:
# zip= int(input("Enter number: "))

# for i in range(1,zip+1):
#     for j in range(i):
#         print(i ,end="")
#     print()



