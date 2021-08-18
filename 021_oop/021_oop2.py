import datetime
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print('\033[31m' + 'some red text')
class Employee:
    # Class variables
    raise_amount = 1.04

    # Regular methods
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @property
    def email(self):
        return self.first_name.lower() + "." + self.last_name.lower() + "@storytellers.com"

    @property
    def Fullname(self):
        return self.first_name + ' ' + self.last_name

    def pay_raise(self):
        self.salary = self.salary * self.raise_amount

    @Fullname.setter
    def Fullname(self, name):
        first, last = name.split()
        self.first_name = first
        self.last_name = last

    @Fullname.deleter
    def Fullname(self):
        print(f'Delete {self.Fullname}')
        self.first_name = None
        self.last_name = None

    def __repr__(self):
        return f"Employee{self.first_name, self.last_name, self.salary}"

    def __str__(self):
        return f"{self.Fullname()}, {self.email}"

    def __add__(self, other):
        return self.salary + other.salary


class Developer(Employee):
    raise_amount = 1.06
    def __init__(self, first_name, last_name, salary, prog_lang):
        super().__init__(first_name, last_name, salary)
        self.prog_lang = prog_lang


class Manager(Employee):
    raise_amount = 1.08
    def __init__(self, first_name, last_name, salary, employees = None):
        super().__init__(first_name,last_name,salary)
        if employees is None:
            self.employees = []
        else:
            if type(employees) == list:
                self.employees = employees
            else:
                raise TypeError

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print(emp.Fullname())




emp1 = Employee('Artur','Ipolitov',2000)
emp2 = Employee('Mary', 'Gold', 2000)
emp3 = Employee('Mark', 'Goldberg', 6000)
emp4 = Employee('He', 'Man', 9000)
emp5 = Employee('Freya', 'Nature', 5000)

dev1 = Developer('Thor', 'Odinsson', 1200, 'Python')
mgr1 = Manager('John','Hughmoungus', 5000)
#
# mgr1.add_employee(dev1)
# print(mgr1.employees)


