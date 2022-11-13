# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 18:30:37 2022

@author: Stephen
"""

annual_salary = float(input('Enter your annual salary: '))
pension_contribution = float(input('Enter your pension contribution %: '))
student_loan_plan_number = float(input('Enter your student loan plan no (0 if no student loan): '))

if annual_salary < 50270:
    PAYE = (annual_salary-12570)*0.2
elif annual_salary <= 150000:
    PAYE = ((annual_salary-(annual_salary-50270)-12570)*0.2) + ((annual_salary-50270)*0.4)
elif annual_salary > 150000:
    PAYE = ((annual_salary-(annual_salary-50270)-12570)*0.2) + ((annual_salary-50270)*0.4) + ((annual_salary-150000)*0.45)
    
if annual_salary < 50270:
    NI = (annual_salary-9568)*0.12
elif annual_salary >= 50270:
    NI = (annual_salary-(annual_salary-50270)-9568)*0.12 + ((annual_salary-50270)*0.02)
    
if student_loan_plan_number == 0:
    SL = 0
elif student_loan_plan_number == 1:
    SL = (annual_salary-(1682*12))*0.09
elif student_loan_plan_number == 2:
    SL = (annual_salary-(2274*12))*0.09

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

