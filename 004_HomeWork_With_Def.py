# 5 0 0 0 5 2 9 2 7 1 9
# 0 1 2 3 4 5 6 7 8 9 10
# 38803160272
import homeWorkFunction

'''
----------------------------------------------------------------------------------------------------
 ------------------------------------- MAIN --------------------------------------------------------
 ----------------------------------------------------------------------------------------------------
'''
user_code = input('Please Enter your ID: ')
condition_user = True
while condition_user:
    user_choice = input('Please choose:\n'

                        '1: ID Data\n'
                        '2: Validate\n'
                        '3: Exit\n'
                        'Enter: ')

    if user_choice == '1':
        homeWorkFunction.data(user_code)
        continue

    elif user_choice == '2':
        homeWorkFunction.validation(user_code)
        continue
    elif user_choice == '3':
        break
    else:
        print("Wrong choice")
        continue

# id_code_array = ["%03d" % x for x in range(1,700+1)]
# print(id_code_array)

'''
----------------------------------------------------------------------------------------------------
 ------------------------------------- MAIN END  ---------------------------------------------------
 ----------------------------------------------------------------------------------------------------
'''