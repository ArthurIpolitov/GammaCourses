'''
Для диапозона чисел 0-100

Если число делится на 3 без остатка - написать Fizz

Если число делится на 5 без остатка - написать Buzz

Если число делится на 3 и на 5 без остатка - написать FizzBuzz
'''
print("---------------------------------------")
user_number = input("Введите число: ")
# user_number = 101
for new_num in range(1, int(user_number) + 1):
    if new_num % 3 == 0 and new_num % 5 == 0:
        # print( str(new_num) + " число делится без остатка на 3 и на 5| Введенное число: " + user_number)
        print("FizzBuzz", new_num)
    elif new_num % 3 == 0:
        # print( str(new_num) + " число делится без остатка на 3| Введенное число: " + user_number)
        print("Fizz", new_num)
    elif new_num % 5 == 0:
        # print( str(new_num) + " число делится без остатка на 5| Введенное число: " + user_number)
        print("Buzz", new_num)