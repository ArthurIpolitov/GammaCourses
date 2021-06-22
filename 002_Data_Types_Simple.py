""" Простые типы данных
# w3schools - references for python
# programiz - info\syntax for python
# Khan Academy - math
"""
# examples

# userAge = 5
# user_age += 3
# print(user_age)

# print(type(user_age)) # Shows data type
# print(help(user_age)) # describes data type of user_age

""" Float Examples """

# pointNumber = 10.56
# intNumber = 5

# print(pointNumber + intNumber)

""" String Examples """

# stringVariable = "Hello"
# stringVariable2 = " World"
# print(stringVariable)
# print(type(stringVariable))

# print ( stringVariable + stringVariable2 )

# x, y, z = 1, 2, 3
# print(x, y, z)

""" Boolean Examples """

# boolValue = True
# print(boolValue)

""" None NoneType Examples """

# nonType = None

""" Conversion """

# a = 10
# print(a)
# print(type(a))
# a = float(a)
# print(type(a))

# a = 123
# b = 1.23
# print(int(a))
# print(float(b))

""" Input Examples """

# name, surname, age = input("Please Enter name, surname, age: ").split(', ') # Splits text
# print(name, surname, age)

""" Round Examples """

# a = 1.5
# b = 2.5
# c = 3.5
#
# print(round(a))
# print(round(b))
# print(round(c))

""" Work """
# a = 100
# b = 2.8
# c = True
# d = None
# e = 'Hello World'
# print(100, 2.8, True, None, 'Hello World')
# print(str(a+b+c+d+e)) #If same type of all

""" Input Work """

# a = input('Please  enter something: ')
# print(a)
# print(type(a))

""" Triangle Prog """

# a, b, c = input("Please Enter Triangle sides : ").split()
# a, b, c = float(a), float(b), float(c)
# perimeter = a + b + c
# halfPerimeter = perimeter / 2
# triangleArea = (halfPerimeter * (halfPerimeter - a) * (halfPerimeter - b) * (halfPerimeter - c)) ** 0.5
# print('Perimeter:', perimeter, '| Half Perimeter:', halfPerimeter, '| Triangle Area:', triangleArea)

""" Name Surname Linn """
import datetime
now = datetime.datetime.now()
name,surname,town,birth_year = input("Please Enter ur Name, Surname, and Birth Year: ").split()
print('Hello,', name, ', Your surname is', surname, ', Your living city is', town,',You are '+ str(now.year - int(birth_year))+' old')
print('Hello', name + ', Your surname is', surname + ', Your living city is', town,',You are '+ str(now.year - int(birth_year))+' old')
