

name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")

basic = float(input("Enter Basic Salary: "))
allowances = float(input("Enter Allowances: "))
overtime = float(input("Enter Overtime Amount: "))
incentives = float(input("Enter Incentives: "))

gross = basic + allowances + overtime + incentives
if gross <= 20000:
    deduction = gross * 0.05
elif gross <= 40000:
    deduction = (20000 * 0.05) + (gross - 20000) * 0.10
else:
    deduction = (20000 * 0.05) + (20000 * 0.10) + (gross - 40000) * 0.15

net_salary = gross - deduction

print("\n========== SALARY STATEMENT ==========")
print("Employee Name :", name)
print("Employee ID   :", emp_id)
print("-------------------------------------")
print("Basic Salary  : Rs.", basic)
print("Allowances    : Rs.", allowances)
print("Overtime      : Rs.", overtime)
print("Incentives    : Rs.", incentives)
print("-------------------------------------")
print("Gross Salary  : Rs.", round(gross, 2))
print("Deductions    : Rs.", round(deduction, 2))
print("-------------------------------------")
print("Net Salary    : Rs.", round(net_salary, 2))
print("=====================================")
