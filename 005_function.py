'''
 ФУНКЦИИ
'''

#
# def square(x):
#     print(int(x) * 2)

# def many_squares(x):
#     for num in x:
#         print(num ** 2)
# many_squares([2, 3, 4, 5, 6, 7, 8])

def print_message(name, surname, age, salary, gender):
    if gender.lower() == 'male':
        result = f'His name is {name} {surname}. He is {age} years old. And his salary is {salary:.2f} eur'
        return print(result)
    elif gender.lower() == 'female':
        result = f'Her name is {name} {surname}. She is {age} years old. And her salary is {salary:.2f} eur'
        return print(result)

# print_message('John', 'Smith', 44, 43059493, 'Male')
# print_message(input("Input name: "), input('Input surname: '), int(input('Input age: ')), int(input('Input Salary: ')), input('Input gender: '))
employees = [['John', ' Smith', 33, 1500, 'male'], ['Anna', ' Smith', 28, 1500, 'female'], ['Artur', ' Smithsson', 28, 700, 'male'], ['John', ' Smith', 33, 1500, 'male'],
             ['Anna', ' Smith', 28, 1500, 'female'], ['Artur', ' Smithsson', 28, 700, 'male']]
# for employer in employees:
#     print_message(employer[0], employer[1], employer[2], employer[3], employer[4])
for name, surname, age, salary, gender in employees:
    print_message(name, surname, age, salary, gender)