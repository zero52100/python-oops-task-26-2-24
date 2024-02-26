class Employee():
    employees_list = []

    def __init__(self, name):
        self.name = name
        self.salary = 0
        Employee.employees_list.append(self)

    def cal_salary(self, hours):
        self.salary = hours * 200

    def __add__(self, other):
        total_expense = Employee(f"Total of {self.name} and {other.name}")
        total_expense.salary = self.salary + other.salary
        return total_expense
class Parttime_Employee(Employee):
    def cal_salary(self, hours):
        self.salary = hours * 150
def cal_average_expense():
    total_salary = sum(employee.salary for employee in Employee.employees_list)
    total_employees = len(Employee.employees_list)
    return total_salary / total_employees if total_employees > 0 else 0
e1_name = input("Enter name for full-time employee 1: ")
e1_hour = int(input("Enter hours worked for full-time employee 1: "))
e1 = Employee(name=e1_name)
e1.cal_salary(hours=e1_hour)
e2_name = input("Enter name for full-time employee 2: ")
e2_hour = int(input("Enter hours worked for full-time employee 2: "))
e2 = Employee(name=e2_name)
e2.cal_salary(hours=e2_hour)
e3_name = input("Enter name for part-time employee 1: ")
e3_hour = int(input("Enter hours worked for part-time employee 1: "))
e3 = Parttime_Employee(name=e3_name)
e3.cal_salary(hours=e3_hour)
print(f"{e1.name} salary: {e1.salary}")
print(f"{e2.name} salary: {e2.salary}")
print(f"{e3.name} salary: {e3.salary}")
total = e1 + e2 + e3
print(f"Total salary expense: {total.salary}")
print(f"Average expense per employee: {cal_average_expense()}")
