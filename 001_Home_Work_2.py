''' ТЗ  '''
''' 
- Пользователь выбирает пункт для обработки
    - Программа смотрит число которое ввёл пользователь, проверяет
    - Выбранны вариант даёт какое-то действие
'''
print("-------------------------------")
print("ВВВЕДИТЕ ЧИСЛО ДЛЯ ВЫБОРА СВОЕЙ ЗАДАЧИ")
print("1 - Математическое сложение двух чисел")
print("2 - Математическое вычитание двух чисел")
print("-------------------------------")


userNum = input("Введите число чтобы выбрать вашу задачу: ")
conA = 1

if int(userNum) == 1:
    digiA = 1
    firstNum = input("Введите первое число: ")
    secondNum = input("Введите второе число: ")
else:
    exit()

if firstNum.isdigit() == True:
    conA = 0
else:
    exit()

if secondNum.isdigit() == True:
    conA = 0
else:
    exit()

if conA == 0:
    finalVar = int(secondNum) + int(firstNum)
    print("Сумма чисел равна: " + str(finalVar))

if int(userNum) == 2:
    digiA = 1
    firstNum = input("Введите первое число: ")
    secondNum = input("Введите второе число: ")
else:
    exit()

if firstNum.isdigit() == True:
    conA = 0
else:
    exit()

if secondNum.isdigit() == True:
    conA = 0
else:
    exit()

if conA == 0:
    finalVar = int(secondNum) - int(firstNum)
    print("Сумма чисел равна: " + str(finalVar))