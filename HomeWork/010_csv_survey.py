import pandas as pd
import time as tm

df = pd.read_csv('survey_results_public.csv')
pd.set_option('display.max_rows', 70000)

def user_menu():
    user_choice = input('Please choose\n'
                        '1. Hobbyist and professionals\n'
                        '2. Minimal age\n'
                        '3. Country\n'
                        '4. Currency Description\n'
                        '5. Exit\n'
                        '------> ')
    if user_choice == '1':
        hobby(df)
    elif user_choice == '2':
        averageminmax(df)
    elif user_choice == '3':
        countrycount(df)
    elif user_choice == '4':
        currencyDesc(df)
    elif user_choice == '5':
        print('Good Bye')
        exit()
    else:
        user_menu()

def hobby(df):
    sorted_values = df[['Hobbyist', 'Respondent']]
    print(sorted_values.groupby('Hobbyist').count())
    tm.sleep(2)
    user_menu()


def averageminmax(df):
    print(f'Average age is {df["Age"].mean()}')
    print(f'Minimal age is {df["Age"].min()}')
    print(f'Max age is {df["Age"].max()}')
    tm.sleep(2)
    user_menu()
def countrycount(df):
    print(f'Countries: {df["Country"].value_counts()}')
    tm.sleep(2)
    user_menu()

def currencyDesc(df):
    print(f'Currency - {df["CurrencyDesc"].value_counts()}')
    tm.sleep(2)
    user_menu()

user_menu()