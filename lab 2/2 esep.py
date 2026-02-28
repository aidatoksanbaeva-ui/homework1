import csv
data=[
    ["name", "department", "salary"],
    ["Ali", "IT", "500000"],
    ["Dana", "HR", "300000"],
    ["Arman", "IT", "600000"],
    ["Aruzhan", "Marketing", "400000"],
    ["Dias", "IT", "450000"]
]
with open("employees.csv", "w", newline="") as f:
    writer=csv.writer(f)
    writer.writerows(data)
employees=[]
departments={}
total_salary=0
c=0
with open("employees.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name=row["name"]
        department=row["department"]
        salary=int(row["salary"])
        employees.append(row)
        total_salary+=salary
        c+=1
        if department not in departments:
            departments[department]=[]
        departments[department].append(salary)
average_salary=total_salary/c
department_average={}
for dept in departments:
    department_average[dept]=sum(departments[dept])/len(departments[dept])
max_dept=""
max_avg=0
for dept in department_average:
    if department_average[dept] > max_avg:
        max_avg=department_average[dept]
        max_dept=dept
max_employee=""
max_salary=0
for emp in employees:
    if int(emp["salary"]) > max_salary:
        max_salary=int(emp["salary"])
        max_employee=emp["name"]
high_salary_employees=[]
for emp in employees:
    if int(emp["salary"]) > average_salary:
        high_salary_employees.append(emp)
with open("high_salary_employees.csv", "w", newline="") as file:
    fieldname = ["name", "department", "salary"]
    writer = csv.DictWriter(file, fieldnames=fieldname)
    writer.writeheader()
    writer.writerows(high_salary_employees)
print("Средняя зарплата:", average_salary)
print("Средняя по отделам:", department_average)
print("Отдел с самой высокой средней зарплатой:", max_dept)
print("Самый высокооплачиваемый сотрудник:", max_employee)
print("Сотрудники выше средней:", [emp["name"] for emp in high_salary_employees])