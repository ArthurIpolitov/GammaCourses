''' ТЗ Для домашней работы '''
''' 
- Пользователь вводит произвольное число -
    - Является ли число четным или не чётным
    - Вычесляет его квадрат и выводит
    - Считает кол-во символов
'''
redCol = "\033[31m"
greenCol = "\033[32m"
endCol = '\033[0m'
yelCol = '\033[33m'

print(yelCol + "--------------Вычисление Четных Чисел-----------------" + endCol)

numberVar = input(yelCol + "Введите число: " + endCol)

if int(numberVar) % 2 == 0:
    # # Вычисления
    squareRootVar = int(numberVar) ** int(numberVar)
    numberLenVar = len(numberVar)
    # #
    # # Проверка на склонения числа
    if str(numberLenVar) == "1" or str(numberLenVar) == "2" or str(numberLenVar) == "3" or str(numberLenVar) == "4":
        con = " символа"
    else:
        con = " символов"
    # #
    # # Вывод данных
    print(greenCol + "Четное число " + numberVar + " ,имеет квадрат числа " + str(squareRootVar) +
          ". Имеет " + str(numberLenVar) + con + endCol)

    # #
else:
    print(redCol + "Число " + numberVar + " нечетное, введите четное число заново" + endCol)

print(yelCol + "------------------Конец Программы---------------------" + endCol)