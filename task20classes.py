# Task 20: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and calculate an individual’s Net Salary using:
#  net_salary = gross_salary - (nhif + nhdf +  nssf + payee)


class Payroll:
   basicsalary = 0
   benefits= 0
   details={}


   def __init__(self,basicsalary,benefits):
        self.basicsalary =basicsalary
        self.benefits =benefits
        self.gross_salary()
        self.nhif()
        self.nssf()
        self.nhdf()
        self.taxable_income()
        self.paye()
        self.net_salary()
        self.add()

        
   
   def gross_salary(self):
       self.gross = self.basicsalary + self.benefits
      
       self.nhif()
   

   def nhif(self):
       self.nhif_contribution1 = 0
       if self.gross <= 0:
        self.nhif_contribution1= 0
       elif self.gross > 0 and self.gross<= 5999:
        nhif_contribution= 150
       elif self.gross >= 6000 and self.gross <= 7999:
        self.nhif_contribution1= 300
       elif self.gross >= 8000 and self.gross < 11999:
        self.nhif_contribution1= 400
       elif self.gross >= 12000 and self.gross <= 14999:
        self.nhif_contribution1= 500
       elif self.gross >= 15000 and self.gross <= 19999:
        self.nhif_contribution1= 600
       elif self.gross >= 20000 and self.gross <= 24999:
        self.nhif_contribution1= 750
       elif self.gross >= 25000 and self.gross <= 29999:
        self.nhif_contribution1= 850
       elif self.gross >= 30000 and self.gross <= 34999:
        self.nhif_contribution1= 900
       elif self.gross >= 35000 and self.gross <= 39999:
        self.nhif_contribution1= 950
       elif  self.gross >= 40000 and self.gross <= 44999:
        self.nhif_contribution1= 1000
       elif self.gross >= 45000 and self.gross <= 49999:
        self.nhif_contribution1= 1100
       elif self.gross >= 50000 and self.gross <= 59999:
        self.nhif_contribution1= 1200
       elif self.gross >= 60000 and self.gross <= 69999:
        self.nhif_contribution1= 1300
       elif self.gross >= 70000 and self.gross <= 79999:
        self.nhif_contribution1= 1400
       elif self.gross >= 80000 and self.gross <= 89999:
        self.nhif_contribution1= 1500
       elif self.gross >= 90000 and self.gross <= 99999:
        self.nhif_contribution1= 1600
       else :
        self.nhif_contribution1= 1700
     

   def nssf(self):
    self.nssf_contribution1=0
    if self.gross < 18000:
       self.nssf_contribution1 = self.gross *  0.06
        
    elif self.gross >= 18000:
       self.nssf_contribution1 = 18000 * 0.06
    else:
        pass
    

   def nhdf(self):
     self.nhdf_contribution1 = 0
     if self.gross < 83334:
        self.nhdf_contribution1 = self.gross * 0.03
     else:
       self.nhdf_contribution1 = 2500
       
     


   def taxable_income(self):
     self.taxableincome1 =  self.gross- (self.nssf_contribution1 + self.nhdf_contribution1)
     
    
   
   def paye(self):
     self.paye1 = 0
     if self.taxableincome1 < 24001:
      self.paye1 = 0
     elif self.taxableincome1 > 24000 and self.taxableincome1 <= 32333:
      self.paye1 = ((2400 + (self.taxableincome1 - 24000) * 0.25) - 2400)
     elif self.taxableincome1 > 32333 and self.taxableincome1 < 500001:
      self.paye1 = ((4483.25 + (self.taxableincome1 - 32333) * 0.3) - 2400)
     elif self.taxableincome1 > 500000 and self.taxableincome1 < 800001:
      self.paye1 = ((144783.25 + (self.taxableincome1 - 500000) * 0.325) - 2400)
     else:
       self.paye1 = (( 242283.35+ (self.taxableincome1 - 800000) * 0.35) - 2400)


   def net_salary(self):
      self.net_salary1 = (self.gross - (self.nhif_contribution1 + self.nhdf_contribution1 + self.nssf_contribution1 + self.paye1))
     
     

   def add(self):
     self.details["Gross Salary"]=self.gross
     self.details["NHIF"]=self.nhif_contribution1
     self.details["NSSF"]=self.nssf_contribution1
     self.details["NHDF"]=self.nhdf_contribution1
     self.details["Taxable Income"]=self.taxableincome1
     self.details["Paye"]=self.paye1
     self.details["Net pay"]=self.net_salary1
    



p1= Payroll(float(input("Enter a basic salary: ")),float(input("Enter a benefits: ")))
print(p1.details)
