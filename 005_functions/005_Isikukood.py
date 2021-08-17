user_id = input('Please enter ID code: ')

while True:
    user_choice = input('Please choose:\n'

                        '1: ID Data\n'
                        '2: Validate\n'
                        '3: Exit\n'
                        'Enter: ')

    if user_choice == '1':
        if int(user_id[0]) % 2 == 0:
            gender = 'Female'
        else:
            gender = 'Male'
        if user_id[0] == '1' or user_id[0] == '2':
                birth_cent = '18'
        if user_id[0] == '3' or user_id[0] == '4':
                birth_cent = '19'
        if user_id[0] == '5' or user_id[0] == '6':
                birth_cent = '20'

        user_birth_region = int(user_id[7:10])
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
    print(
        f'Your gender is {gender}. Birth date is {user_id[5:7]}.{user_id[3:5]}.{birth_cent}{user_id[1:3]} and birth region is {region}')
        continue
    elif user_choice == '2':

        continue
    elif user_choice == '3':
        break
    else:
        print("Wrong choice")
        continue