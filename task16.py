# TASK 16: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate using. Compute NSSF using 6% of the Gross Salary. BUT ONLY A MAXIMUM OF 18,000
# CAN BE USED IN NSSF. 


basicsalary= float(input("Enter a basic salary: "))
benefits= float(input("Enter a benefits: "))

gross = basicsalary + benefits
print("Gross Slary is: ",gross)
nhif_contribution = 0

if gross <= 0:
        print("NHIF is: 0")
elif gross > 0 and gross<= 5999:
        print("NHIF is: 150")
elif gross >= 6000 and gross <= 7999:
        print("NHIF is: 300")
elif gross >= 8000 and gross < 11999:
        print("NHIF is: 400")
elif gross >= 12000 and gross <= 14999:
        print("NHIF is: 500")
elif gross >= 15000 and gross <= 19999:
        print("NHIF is: 600")
elif gross >= 20000 and gross <= 24999:
        print("NHIF is: 750")
elif gross >= 25000 and gross <= 29999:
        print("NHIF is: 850")
elif gross >= 30000 and gross <= 34999:
        print("NHIF is: 900")
elif gross >= 35000 and gross <= 39999:
        print("NHIF is: 950")
elif  gross >= 40000 and gross <= 44999:
        print("NHIF is: 1000")
elif gross >= 45000 and gross <= 49999:
        print("NHIF is: 1100")
elif gross >= 50000 and gross <= 59999:
        print("NHIF is: 1200")
elif gross >= 60000 and gross <= 69999:
        print("NHIF is: 1300")
elif gross >= 70000 and gross <= 79999:
        print("NHIF is: 1400")
elif gross >= 80000 and gross <= 89999:
        print("NHIF is: 1500")
elif gross >= 90000 and gross <= 99999:
        print("NHIF is: 1600")
else :
        print("NHIF is: 1700")
        



nssf_contribution = 0
if gross < 18000:
    nssf_contribution = gross *  0.06
    print("NSSF is: ", nssf_contribution)

elif gross >= 18000:
        nssf_contribution = 18000 * 0.06
        print("NSSF is: ", nssf_contribution)

else:
        pass