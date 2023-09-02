# TASK 7: Using Python or PHP or Java or Ruby or JavaScript
# Write that prompts the user to input student marks. The input should be between 0 and 100.
# Then output the correct grade: 
# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40

marks= int(input("Enter marks: "))

if marks>79 and marks<=100:
    print("A")
elif marks>=60 and marks<=79:
    print("B")
elif marks>=49 and marks<60:
    print("C")
elif marks>=40 and marks<50:
    print("D")
elif marks<40:
    print("E")
else:
    pass