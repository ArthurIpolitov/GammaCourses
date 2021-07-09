import datetime as dt

user_bd = int(input("Input your day of birth: "))
user_bm = int(input("Input your month of birth: "))
user_by = int(input("Input your year of birth: "))

dt_today = dt.date.today()
user_birthday = dt.date(user_by, user_bm, user_bd)
print(user_birthday