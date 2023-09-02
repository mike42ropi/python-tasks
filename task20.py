# Task 20: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and calculate an individual’s Net Salary using:
#  net_salary = gross_salary - (nhif + nhdf +  nssf + payee)

basicsalary= float(input("Enter a basic salary: "))
benefits= float(input("Enter a benefits: "))

gross = basicsalary + benefits
print("Gross Slary is: ",gross)
nhif_contribution = 0


# NHIF
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
        

# NSSF

nssf_contribution = 0
if gross < 18000:
    nssf_contribution = gross *  0.06
    print("NSSF is: ", nssf_contribution)

elif gross >= 18000:
        nssf_contribution = 18000 * 0.06
        print("NSSF is: ", nssf_contribution)

else:
        pass


# NHDF
nhdf_contribution = 0
if gross < 83334:
    nhdf_contribution = gross * 0.03
    print("NHDF is: ",nhdf_contribution)
else:
    print("NHDF is: 2500")

# Taxable Income
ti =  gross- (nssf_contribution + nhdf_contribution)
print("Taxable Income is:",ti)

# PAYE
paye = 0

if ti < 24001:
    paye = 0
    print("PAYE is:",paye)
elif ti > 24000 and ti <= 32333:
    paye = ((2400 + (ti - 24000) * 0.25) - 2400)
    print("PAYE is:",paye)
elif ti > 32333 and ti < 500001:
    paye = ((4483.25 + (gross - 32333) * 0.3) - 2400)
    print("PAYE is:",paye)
elif gross > 500000 and gross < 800001:
    paye = ((144783.25 + (gross - 500000) * 0.325) - 2400)
    print("PAYE is:",paye)
else:
       paye = (( 242283.35+ (gross - 800000) * 0.35) - 2400)
       print("PAYE is:",paye)


# Net Salary
net_salary = (gross - (nhif_contribution + nhdf_contribution + nssf_contribution + paye))
print("Net Salary is:", net_salary)