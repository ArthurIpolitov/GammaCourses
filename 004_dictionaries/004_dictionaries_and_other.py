'''
Словари и прочие управляющие функции
'''
# DICTIONARY EXAMPLE
x = 5
student = {'name': 'John', 'age': 32, 'courses': ['Math', 'Art', 'Programming'],
           1: 'int key', 0.2: 'float key', x: 'variable', 'var key': x}

''' GET NEW KEY '''

# user_input = input("Please enter key: ")
#
# if student.get(user_input, 'Not Found') == 'Not Found':
#     student[user_input] = input(f"Please enter: ")
#
# print(student[user_input])

''' UPDATE DICTIONARY '''

# new_dict = {'surname': 'Smith', 'phone': '555-555-555'}
# student.update(new_dict)
# print(student)

''' DELETE KEY AND VAR '''
# del student['name']
# print(student)

''' VALUES AND ITEMS AND KEYS'''
# print(student.values())
# print(student.items())
# print(student.keys())
# for key, value in student.items():
#     print(key, value)

# workers = [('Alex', 'Smith', '32', 'male'), ('John', 'MacDouglas', '44', 'male'), ('Mary', 'Dudes', '54', 'female')]
#
# for name, surname, age, gender in workers:
#     if gender == 'male':
#         print(f'This is {name} {surname}, he is {age} years old')
#     elif gender == 'female':
#         print(f'This is {name} {surname}, she is {age} years old')
    # print(f'This is {worker[0]} {worker[1]}, he is {worker[2]} years old')

''' WHILE '''

# x = 20
# while x > 0:
#     time.sleep(1)
#     print(f"Before detonation {x} sec")
#     if x == 1:
#         print("BOOM")
#     x -= 1


# distance_to_target = float(input('Input distance to target: '))
# foot = 0.5
# current_position = 0
# cnt = 0
#
# while current_position != distance_to_target * 1000:
#     current_position += foot
#     cnt += 1
#
#
# print(current_position)
# print(cnt)

''' MENU '''
#
# while True:
#     user_choice = input('Please choose:\n'
#                         '1: Print Hello\n'
#                         '2: Print World\n'
#                         '3: Exit\n'
#                         'Enter: ')
#     if user_choice == "1":
#         print("Hello")
#     elif user_choice == "2":
#         print("World")
#     elif user_choice == "3":
#         break
#     else:
#         print('Wrong choice')

# for letter in 'Python':
#     if letter == 't':
#         print('Reached letter "t"')
#     else:
#         continue
# while True:
#     try:
#         user_input = input("Please enter your ID: ")
#         if len(user_input) != 11:
#             raise UserWarning
#         user_input = int(user_input)
#     except ValueError:
#         print('ID Code you entered is not numeric')
#         continue
#     except UserWarning:
#         print("ID you entered is wrong")
#         continue
#     # else:
#     #     print('Your ID Code is', user_input)
#     #     break
#     # finally:
#     #     print("Good Bye")
#     break


user_code = input('Please Enter your ID: ')
user_choice = input('Please choose:\n'
                    
                    '1: ID Data\n'
                    '2: Validate\n'
                    '3: Exit\n'
                    'Enter: ')

if user_choice == '1':
    if int(user_code[0]) % 2 == 0:
        gender = 'Female'
    else:
        gender = 'male'
    if user_code[0] == '1' or user_code[0] == '2':
        birth_cent = '19'
    if user_code[0] == '3' or user_code[0] == '4':
        birth_cent = '20'

elif user_choice == '2':
    pass
elif user_choice  == '3':
    pass
else:
    print("Wrong choice")