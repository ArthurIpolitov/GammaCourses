'''
МОДУЛИ И БИБЛИОТЕКИ
'''
# import time
# import datetime
# import date

import datetime as dt

# time.sleep(5)
# print('Hello')
# time.sleep(5)
# print('World')
#
# start = time.time()
# time.sleep(5)
# stop = time.time()
# print(stop - start)
# print(time.time())

# while True:
#     print(time.gmtime())
#     time.sleep(1)
# print(time.gmtime()[:3])

# print(time.asctime().split())


# print(dt.date.today())
# d = dt.date(2021, 7, 7)
# till_bd = dt.date(2022, 5, 29)
# print(till_bd - d)

# today = dt.date.today()
# some_date = dt.date(1990, 10, 7)
# print(some_date.weekday())
# print(some_date.isoweekday())

# tdelta = dt.timedelta(days=7)
# today = dt.date.today()
# print(today + tdelta)

# today1 = dt.date.today()
# bday1 = dt.date(2022,3,16)
# delta_time = bday1 - today1
# print(delta_time.total_seconds())

# t = dt.time(17, 0, 45)
# print(t)
#
#
# print(t.hour)
#
# tdelta = dt.timedelta(days=7,hours=5,minutes=40,seconds=10)
# today = dt.datetime.today()
# date1 = today + tdelta
# date2 = today + tdelta
# print(date1 == date2)

dt_str = 'November 30, 2020, 15:45'
dt_str1 = '12:28:33 Nov 30, 2020'
dt_str2 = 'Wed, 07/07/21'
today = dt.datetime.now()
# print(today.strftime('%A, %d %B %Y'))
# str_to_date = dt.datetime.strptime(dt_str, '%B %d, %Y')
# print(str_to_date)
str_to_date1 = dt.datetime.strptime(dt_str, '%B %d, %Y, %H:%M')
print(str_to_date1)
str_to_date2 = dt.datetime.strptime(dt_str1,'%H:%M:%S %b %d, %Y')
print(str_to_date2)
str_to_date3 = dt.datetime.strptime(dt_str2, '%a, %m/%d/%y')
print(str_to_date3)