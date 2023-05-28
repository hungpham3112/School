class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"""
Name: {self.name}
Age: {self.age}
Salary: {self.salary}
"""


lst = []
while True:
    try:
        number = int(input("Enter the number of employees: "))
    except ValueError:
        print("Please enter a number!")
        continue
    for i in range(1, number + 1):
        print(f"Enter employees: {i}")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        salary = int(input("Enter salary: "))
        employee = Employee(name, age, salary)
        lst.append(employee)
    print("\nList before sorting:")
    for index, employee in enumerate(lst):
        print(f"Employees  {index + 1}{repr(employee)}")
    print("\nList after sorting:")
    for index, employee in enumerate(sorted(lst, key=lambda x: x.age, reverse=True)):
        print(f"Employees  {index + 1}{repr(employee)}")
    break
