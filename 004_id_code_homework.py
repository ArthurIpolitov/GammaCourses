""" ТЗ
Домашнее задание:
Написать программу которая берёт у пользователя ISIKUKOOD и предоставляет пользователю выбор:
1. Разобрать код и вывести данный о человеке чей код введён (пол, дата рождения итд)
2. Проверяет валидность кода
3. Выходит из программы

В идеале должна быть проверка, чтобы пользователь ввёл именно ISIKUKOOD
В идеале у пользователя должна быть возможность сделать выбор повторно, не перезапуская программу.
"""
# birth_place = ()
# user_code = input('Please Enter your ID: ')
# user_choice = input('Please choose:\n'
#
#                     '1: ID Data\n'
#                     '2: Validate\n'
#                     '3: Exit\n'
#                     'Enter: ')
#
# if user_choice == '1':
#     if int(user_code[0]) % 2 == 0:
#         gender = 'Female'
#     else:
#         gender = 'Male'
#     if user_code[0] == '1' or user_code[0] == '2':
#         birth_cent = '18'
#     if user_code[0] == '3' or user_code[0] == '4':
#         birth_cent = '19'
#     if user_code[0] == '5' or user_code[0] == '6':
#         birth_cent = '20'
#     print(f"Your gender is {gender} and birthday date is {user_code[5:7]}.{user_code[3:5]}.{birth_cent}{user_code[1:3]}")
#
# elif user_choice == '2':
#     pass
# elif user_choice == '3':
#     pass
# else:
#     print("Wrong choice")

id_code = "50005292719"
id_code_array=["%03d" % x for x in range(1,700+1)]
print(id_code_array)