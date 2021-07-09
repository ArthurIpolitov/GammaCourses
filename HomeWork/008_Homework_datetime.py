import datetime as dt

user_bd = int(input("Input your day of birth: "))
user_bm = int(input("Input your month of birth: "))
user_by = int(input("Input your year of birth: "))
# YEARS OLD
dt_today = dt.date.today()
user_birthday = dt.date(user_by, user_bm, user_bd)
bday_result = dt_today.year - user_birthday.year
# DAYS TO NEXT BD
days_until_bd = dt.date(dt_today.year+1, user_bm,user_bd) - dt_today
# DAYS FROM LAST BD
last_birthday = dt.date(dt_today.year, user_bm, user_bd)
last_bd_result = dt_today - last_birthday

print(f"Days from last birthday is {last_bd_result.days} days")
print(f"Days to next birthday is {days_until_bd.days} days")
print(f"Your age is {bday_result} years old")
