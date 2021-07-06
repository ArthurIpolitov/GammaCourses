# 5 0 0 0 5 2 9 2 7 1 9
# 0 1 2 3 4 5 6 7 8 9 10
# 38803160272
condition_user = True

user_code = input('Please Enter your ID: ')
while condition_user:
    user_choice = input('Please choose:\n'
    
                    '1: ID Data\n'
                    '2: Validate\n'
                    '3: Exit\n'
                    'Enter: ')

    if user_choice == '1':
        # -------------------------
        # GENDER CHOICE
        if int(user_code[0]) % 2 == 0:
            gender = 'Female'
        else:
            gender = 'Male'
        # GENDER CHOICE END
        # --------------------------
        # BIRTHDAY CENTURY
        if user_code[0] == '1' or user_code[0] == '2':
            birth_cent = '18'
        if user_code[0] == '3' or user_code[0] == '4':
            birth_cent = '19'
        if user_code[0] == '5' or user_code[0] == '6':
            birth_cent = '20'
        # BIRTHDAY CENTURY END
        # --------------------------
        # BIRTH REGION
        user_birth_region = int(user_code[7:10])
        if user_birth_region >= 0 and user_birth_region <= 10:
            region = 'Kuressaare haigla'
        elif user_birth_region >= 11 and user_birth_region <= 19:
            region = 'Tartu Ülikooli Naistekliinik'
        elif user_birth_region >= 21 and user_birth_region <= 150:
            region = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
        elif user_birth_region >= 151 and user_birth_region <= 160:
            region = 'Keila haigla'
        elif user_birth_region >= 161 and user_birth_region <= 220:
            region = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
        elif user_birth_region >= 221 and user_birth_region <= 270:
            region = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
        elif user_birth_region >= 271 and user_birth_region <= 370:
            region = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
        elif user_birth_region >= 371 and user_birth_region <= 420:
            region = 'Narva haigla'
        elif user_birth_region >= 421 and user_birth_region <= 470:
            region = 'Pärnu haigla'
        elif user_birth_region >= 471 and user_birth_region <= 490:
            region = 'Haapsalu haigla'
        elif user_birth_region >= 491 and user_birth_region <= 520:
            region = 'Järvamaa haigla (Paide)'
        elif user_birth_region >= 521 and user_birth_region <= 570:
            region = 'Rakvere haigla, Tapa haigla'
        elif user_birth_region >= 571 and user_birth_region <= 600:
            region = 'Valga haigla'
        elif user_birth_region >= 601 and user_birth_region <= 650:
            region = 'Viljandi haigla'
        elif user_birth_region >= 651 and user_birth_region <= 700:
            region = 'Lõuna-Eesti haigla (Võru), Põlva haigla'
        # BIRTH REGION EN
        # --------------------------
        print(f'Your gender is {gender}. Birth date is {user_code[5:7]}.{user_code[3:5]}.{birth_cent}{user_code[1:3]} and birth region is {region}')
        continue

    elif user_choice == '2':
        if len(user_code) != 11:
            print('Invaid')
        else:
            first_formula = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
            second_formula = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
            controll_number = int(user_code[0]) * first_formula[0] + int(user_code[1]) * first_formula[1] + int(user_code[2]) * first_formula[2] + int(user_code[3]) * first_formula[3] + int(user_code[4]) * first_formula[4] + int(user_code[5]) * first_formula[5] + int(user_code[6]) * first_formula[6] + int(user_code[7]) * first_formula[7] + int(user_code[8]) * first_formula[8] + int(user_code[9]) * first_formula[9]
            controll_left = controll_number % 11
            # --------------------------
            # CONTROLL LEFT VALID
            if controll_left == 10:
                # IF CONTROLLNUMBER LEFT IS 10
                controll_number = int(user_code[0]) * second_formula[0] + int(user_code[1]) * second_formula[1] + int(user_code[2]) * second_formula[2] + int(user_code[3]) * second_formula[3] + int(user_code[4]) * second_formula[4] + int(user_code[5]) * second_formula[5] + int(user_code[6]) * second_formula[6] + int(user_code[7]) * second_formula[7] + int(user_code[8]) * second_formula[8] + int(user_code[9]) * second_formula[9]
                controll_left = controll_number % 11
                print(str(controll_left))
                if str(controll_left) == user_code[10]:
                    print('Valid == 0')
                else:
                    print('Invalid == 0')
                # IF CONTROLLNUMBER LEFT IS 10 END
                # -------------------------------
                # IF CONTROLLNUMBER LEFT IS FINE
            elif controll_left != 0:
                print(str(controll_left))
                if str(controll_left) == user_code[10]:
                    print('Valid != 0')
                else:
                    print('Invalid != 0')
                # IF CONTROLLNUMBER LEFT IS FINE END
                # -------------------------------
            # CONTROLL LEFT VALID END
            # --------------------------
            # KONTROLLNUMBER VALIDATION
            # control_number =
            continue
    elif user_choice == '3':
        break
    else:
        print("Wrong choice")
        continue

# id_code_array = ["%03d" % x for x in range(1,700+1)]
# print(id_code_array)

