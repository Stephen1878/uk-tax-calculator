# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 18:30:37 2022

@author: Stephen
"""

annual_salary = float(input('Enter your annual salary: '))
pension_contribution = float(input('Enter your pension contribution %: '))

if annual_salary < 50270:
    PAYE = (annual_salary-12570)*0.2
elif annual_salary >= 50270:
    PAYE = ((annual_salary-(annual_salary-50270)-12570)*0.2) + ((annual_salary-50270)*0.4)
    
if annual_salary < 50270:
    NI = (annual_salary-9568)*0.12
elif annual_salary >= 50270:
    NI = (annual_salary-(annual_salary-50270)-9568)*0.12 + ((annual_salary-50270)*0.02)
    
SL = (annual_salary-(1657*12))*0.09
pension = annual_salary * (pension_contribution/100)
total_deductions = PAYE+NI+SL+pension
net_salary = annual_salary - total_deductions
monthly_net_salary = net_salary/12

print('Annual Salary:',annual_salary)
print('PAYE:',PAYE)
print('NI:',NI)
print('Student Loan Payments:',SL)
print('Pension Contributions:',pension)
print('total_deductions:',total_deductions)
print('Net Annual Salary:',net_salary)
print('Monthly Net Salary:',monthly_net_salary)

