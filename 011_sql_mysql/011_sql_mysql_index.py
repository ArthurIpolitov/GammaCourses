import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='12345',
    database='happiness_schema'
)
# df = pd.read_sql_query('SELECT country_or_region, score FROM happiness', mydb)
# print(df['country_or_region'])

# dbcursor = mydb.cursor()

# dbcursor.execute('CREATE SCHEMA students')
# dbcursor.execute('CREATE TABLE student (name VARCHAR(255), surname VARCHAR(255), age INTEGER(10))')
# dbcursor.execute('INSERT INTO student (name, surname, age) VALUES ("JACK", "SMITH", 32)')
# mydb.commit()
# first = input("Input Student Info: ")
# second = input("Input Student Info: ")
# third = input("Input Student Info: ")
#
# sql_formula = 'INSERT INTO student (name, surname, age) VALUES (%s, %s, %s)'
# student1 = (first,second, int(third))
# dbcursor.execute(sql_formula, student1)
# mydb.commit()

# cursor = mydb.cursor()
# cursor.execute('SELECT * FROM happiness')
# result = cursor.fetchall()
# for row in result:
#     print(f'------------------ Number {row[0]} - {row[1]} ---------------------')
#     print(f'1.Country: {row[1]}\n'
#           f'2.Score: {row[2]}\n'
#           f'3.GDPpc: {row[3]}\n'
#           f'4.Social Support: {row[4]}\n'
#           f'5.Healthy Life Exp: {row[5]}\n'
#           f'6.Freedom to make life choices: {row[6]}\n'
#           f'7.Generosity: {row[7]}\n'
#           f'8.Perception of Corruption: {row[8]}')
#     print('-----------------------------------------------------------------')