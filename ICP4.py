"""
John Widner
ICP 4
06-14-18
"""



class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):  # Inherits from Class Person

    number_of_employees = 0
    family = {}

    def __init__(self, name, age, family, salary, department):
        super().__init__(name=name, age=age)
        self.family = family  # Set family
        self.salary = salary  # Set salary
        self.department = department
        self.increment_employee_count()

    # Sets
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_salary(self, salary):
        self.salary = salary

    def set_department(self, department):
        self.department = department

    # Gets
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_salary(self):
        return self.salary

    def get_department(self):
        return self.department

    def increment_employee_count(self):
        self.number_of_employees += 1


class FullTimeEmployee(Employee):  # Inherits from Employee AND Person

    def __init__(self, name, age, family, salary, department):
        super().__init__(name=name, age=age, family=family, salary=salary, department=department)

    def increment_employee_count(self):  # Overloaded function from Employee
        self.number_of_employees += 2


Person('John', 37)

Steve = Employee('Steve', 45, 5, 40000, 'sales')

print(Steve.get_name())
print(Steve.get_age())
print(Steve.number_of_employees)

Bill = FullTimeEmployee('Bill', 55, 5, 50000, 'marketing')

print(Bill.get_name())
print(Bill.get_age())
print(Bill.number_of_employees)

"""
Question 2 10x10 Array


random_array = numpy.random.rand(10, 10)

def findMaxMin():
    if index >= 10:
        return
    else:
        Min = min(random_array + 1)
        Max = max(random_array + 1)

    print(str(Min), str(Max))
"""