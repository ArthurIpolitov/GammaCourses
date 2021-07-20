import pandas as pd
import numpy as np

df = pd.read_csv('survey_results_public.csv')

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
        pass
    elif user_choice == '4':
        pass
    elif user_choice == '5':
        print('Good Bye')
        exit()
    else:
        user_menu()

def hobby(df):
    print('soon')


def averageminmax(df):
    print(f'Average age is {df["Age"].mean()}')
    print(f'Minimal age is {df["Age"].min()}')
    print(f'Max age is {df["Age"].max()}')

user_menu()