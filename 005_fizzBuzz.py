def fizzBuzz(range_user, end_range_user):
    for new_num in range(int(range_user), int(end_range_user) + 1):
        if new_num % 3 == 0 and new_num % 5 == 0:
            # print( str(new_num) + " число делится без остатка на 3 и на 5| Введенное число: " + user_number)
            print("FizzBuzz", new_num)
        elif new_num % 3 == 0:
            # print( str(new_num) + " число делится без остатка на 3| Введенное число: " + user_number)
            print("Fizz", new_num)
        elif new_num % 5 == 0:
            # print( str(new_num) + " число делится без остатка на 5| Введенное число: " + user_number)
            print("Buzz", new_num)

fizzBuzz(input("Input star Number: "), input("Input end Number: "))