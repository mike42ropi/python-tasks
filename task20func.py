basicsalary= float(input("Enter a basic salary: "))
benefits= float(input("Enter a benefits: "))

def gross_salary(basicsalary, benefits):
       gross1 = basicsalary + benefits
       return gross1
gross=gross_salary(basicsalary, benefits) 
print("Gross Slary is: ",gross)



# NHIF
def nhif(gross):
       nhif_contribution1 = 0
       if gross <= 0:
        nhif_contribution1= 0
       elif gross > 0 and gross<= 5999:
        nhif_contribution= 150
       elif gross >= 6000 and gross <= 7999:
        nhif_contribution1= 300
       elif gross >= 8000 and gross < 11999:
        nhif_contribution1= 400
       elif gross >= 12000 and gross <= 14999:
        nhif_contribution1= 500
       elif gross >= 15000 and gross <= 19999:
        nhif_contribution1= 600
       elif gross >= 20000 and gross <= 24999:
        nhif_contribution1= 750
       elif gross >= 25000 and gross <= 29999:
        nhif_contribution1= 850
       elif gross >= 30000 and gross <= 34999:
        nhif_contribution1= 900
       elif gross >= 35000 and gross <= 39999:
        nhif_contribution1= 950
       elif  gross >= 40000 and gross <= 44999:
        nhif_contribution1= 1000
       elif gross >= 45000 and gross <= 49999:
        nhif_contribution1= 1100
       elif gross >= 50000 and gross <= 59999:
        nhif_contribution1= 1200
       elif gross >= 60000 and gross <= 69999:
        nhif_contribution1= 1300
       elif gross >= 70000 and gross <= 79999:
        nhif_contribution1= 1400
       elif gross >= 80000 and gross <= 89999:
        nhif_contribution1= 1500
       elif gross >= 90000 and gross <= 99999:
        nhif_contribution1= 1600
       else :
        nhif_contribution1= 1700
       return nhif_contribution1 
        
nhif_contribution=nhif(gross)
print(f"NHIF is: {nhif_contribution}")



# NSSF
def nssf(gross):
   nssf_contribution1 = 0
   if gross < 18000:
    nssf_contribution1 = gross *  0.06
    print("NSSF is: ", nssf_contribution)
   elif gross >= 18000:
     nssf_contribution1 = 18000 * 0.06
   else:
        pass

   return nssf_contribution1

nssf_contribution= nssf(gross)
print(f"NSSF is:{nssf_contribution}")



# NHDF
def nhdf(gross):
   nhdf_contribution1 = 0
   if gross < 83334:
    nhdf_contribution1 = gross * 0.03
    
   else:
    nhdf_contribution1 = 2500
   return nhdf_contribution1

nhdf_contribution=nhdf(gross)
print(f"NHDF is:{nhdf_contribution}")

# Taxable Income
def taxable_income(gross,nssf_contribution,nhdf_contribution):
  ti1 =  gross- (nssf_contribution + nhdf_contribution)
  return ti1

ti=taxable_income(gross,nssf_contribution,nhdf_contribution)
print(f"Taxable Income is:{ti}")

# PAYE
def paye1(ti):
  paye2 = 0
  if ti < 24001:
    paye2 = 0
    
  elif ti > 24000 and ti <= 32333:
    paye2 = ((2400 + (ti - 24000) * 0.25) - 2400)
    
  elif ti > 32333 and ti < 500001:
    paye2 = ((4483.25 + (gross - 32333) * 0.3) - 2400)
    
  elif ti > 500000 and ti < 800001:
    paye2 = ((144783.25 + (ti - 500000) * 0.325) - 2400)
    
  else:
       paye2 = (( 242283.35+ (ti - 800000) * 0.35) - 2400)
  return paye2
  

paye =paye1(ti)
print(f"PAYE is:{paye}")      

# Net Salary
def net_salary1(gross,nhif_contribution,nhdf_contribution,nssf_contribution,paye):
  net_salary = (gross - (nhif_contribution + nhdf_contribution + nssf_contribution + paye))
  return net_salary


the_netsalary= net_salary1(gross,nhif_contribution,nhdf_contribution,nssf_contribution,paye)
print(f"Net Salary is:{the_netsalary}")