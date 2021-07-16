'''
1. Программа выводит топ стран по GDP per capita
2. Программа выводит строку по названию страны (вводит пользователь)
3. Программа определяет есть ли одинаковые значения в столбце Generosity
'''
import pandas as pd
import time as tm
df = pd.read_csv('2019.csv')

def user_menu():
    user_choice = input('Please choose\n'
          '1. Top GDP countries\n'
          '2. Data by country name\n'
          '3. Check if there are equal values in Generosity\n'
          '0.Exit\n'
          '------> ')
    if user_choice == '1':
        topten(df)
    elif user_choice == '2':
        country_data(df)
    elif user_choice == '3':
        check_doubles(df)
    elif user_choice == '0':
        print('...................')
        print('.....Good bye!.....')
        print('...................')
        exit()
    else:
        print('......WAITING......')
        tm.sleep(2)
        print('INPUT VALID CHOICE')
        tm.sleep(2)
        print('...................')
        user_menu()


def topten(df):
    try:
        print('...................')
        top = abs(int(input('How many values?: ')))
        if top > df.shape[0]:
            print(f'THERE ARE LESS ENTRIES IN DF, SHOWING {df.shape[0]} ENTRIES')
            top = df.shape[0]
        print('...................')
    except:
        print('...................')
        print('.....TRY AGAIN.....')
        topten(df)
    print(df.sort_values('GDP per capita', ascending=False).head(top))
    print('...................')
    us_ch = input('RETURN TO CHOICE?\n'
                  '1. YES\n'
                  '2. NO\n'
                  '3. EXIT\n'
                  '-----> ')
    if us_ch == '1':
        user_menu()
    elif us_ch == "2":
        topten(df)
    elif us_ch == '3':
        print('...................')
        print('.....Good bye!.....')
        print('...................')
        exit()


def country_data(df):
    try:
        print('..............')
        country = input('PLEASE ENTER COUNTRY NAME: ')
        if country in df['Country or region'].values:
            print(df.loc[df['Country or region'] == country])
        else:
            raise UserWarning
    except:
        print('INVALID COUNTRY NAME, ENTER NEW')
        choice = input('WOULD U LIKE TO SEE LIST OF COUNTRIES? Y/N: ')
        if choice == 'Y':
            print(df['Country or region'].values)

        elif choice == 'N':
            print('RETURN TO MAIN MENU')
            user_menu()
        else:
            print("WRONG CHOICE")
            user_menu()


def check_doubles(df):
    new_df = df.groupby('Generosity').sum()
    if df.shape[0] != new_df.shape[0]:
        print("..............................................")
        print('THERE ARE SAME VALUES IN GENEROSITY COLUMN')
        print("..............................................")
    else:
        print("..............................................")
        print('THERE ARE NO SAME VALUES IN GENEROSITY COLUMN')
        print("..............................................")
    user_menu()



user_menu()