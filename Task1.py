class Employee():
    def __init__(self, name):
        self.name = name
        self.salary = 0

    def cal_salary(self, hours):
        self.salary = hours * 200

    def __add__(self, other):
        total_expense = Employee(f"Total of {self.name} and {other.name}")
        total_expense.salary = self.salary + other.salary
        return total_expense

class Parttime_Employee(Employee):
    def cal_salary(self, hours):
        self.salary = hours * 150

e1_name = input("Enter name for full-time employee 1: ")
e1_hour = int(input("Enter hours worked for full-time employee 1: "))

e1 = Employee(name=e1_name )
e1.cal_salary(hours=e1_hour )

e2_name  = input("Enter name for full-time employee 2: ")
e2_hour = int(input("Enter hours worked for full-time employee 2: "))

e2 = Employee(name=e2_name)
e2.cal_salary(hours=e2_hour)

e3_name = input("Enter name for part-time employee 1: ")
e3_hour = int(input("Enter hours worked for full-time employee 2: "))

e3 = Parttime_Employee(name=e3_name)
e3.cal_salary(hours=e3_hour)
print(f"{e1_name} salary : {e1.salary} ")
print(f"{e2_name} salary : {e2.salary} ")
print(f"{e3_name} salary : {e3.salary} ")
total = e1 + e2 + e3

print(f"Total expense: {total.salary}")
