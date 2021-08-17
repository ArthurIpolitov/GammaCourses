import datetime

class Employee:
    #Class variables
    raise_amount = 1.0
    number_of_employees = 0

    # Regular methods
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = first_name.lower() + "." + last_name.lower() + "@storytellers.com"

        Employee.number_of_employees += 1

    def Fullname(self):
        return self.first_name + ' ' + self.last_name
    
    def pay_raise(self):
        self.salary = self.salary * self.raise_amount

    @classmethod
    def from_string(cls, emp_string):
        first_name, last_name, salary = emp_string.split('-')
        return cls(first_name,last_name,salary)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



        
emp1 = Employee('Artur','Ipolitov',2000)
emp2 = Employee('Mary', 'Gold', 2000)
emp3 = Employee('Mark', 'Goldberg', 6000)
emp4 = Employee('Thor', 'Odinsson', 9000)
emp5 = Employee('Freya', 'Nature', 5000)

some_date = datetime.date(2021, 8, 17)
print(Employee.is_workday(some_date))
#
# emp6_string = 'John-Kennedy-1000000'
# emp7 = 'Bob-Dylan-1974'
#
# emp6 = Employee.from_string(emp6_string)
# print(emp6.__dict__)
#
#
#
#
#



# print('----------------------')
# print('EMPLOYEE LIST')
# print('----------------------')
#
# def choice():
#     Choice = input('What you want to do?\n'
#                 '1. List of all Employees\n'
#                 '2. Add new Employee\n'
#                 '3. Exit\n'
#                     '-----> ')
#
#     if Choice == '1':
#         listEmployees()
#     elif Choice == '2':
#         pass
#     elif Choice == '3':
#         exit()
#
# def listEmployees():
#     emplnum = 1
#     for empl in Employee.__dict__:
#         print(Employee.Fullname(emp1))





# Employee.raise_amount = 1.08
# emp1.raise_amount = 1.06
# emp1.pay_raise()
# emp2.pay_raise()
# print(emp1.salary)
# print(emp2.salary)
# print(emp1.email)
# print(emp1.Fullname())
# print(emp1.salary)
# emp1.pay_raise()
# print(emp1.salary)

# choice()

#---------------------------------
# emp1 = Employee()
# emp2 = Employee()
#
# emp1.first_name = 'Roman'
# emp1.age = 33
# emp1.email = 'roman@gmai.com'
# ---------------------------------
