# TASK 1: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prompts the user to enter the base and height of a triangle and returns its area.
base = float(input("Enter Base: "))
height = float(input("Enter Height: "))   
def triangle_area(base,height):

    area = 1/2*base*height
    return area


result =triangle_area(base,height)
print(result)

