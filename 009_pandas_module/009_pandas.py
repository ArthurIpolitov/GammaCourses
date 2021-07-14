import pandas as pd

df = pd.read_csv('2019.csv')
# # pd.set_option('display.max_columns', 9)
# # pd.set_option('display.max_rows', 136)
# print(df)
# df.to_csv('new_csv', columns=["Overall rank","GDP per capita","Perceptions of corruption"])
# people = {
#     'name':['Bob','Mary','John','Sarah'],
#     "surname":['Smith','Gold','Watson','Brown'],
#     'email':['bot.smith@gmail.com','mary.gold@gmail.com','john.watson@gmail.com','sarah.brown@gmail.com']
# }
#
# df = pd.DataFrame(people)
# print(df.iloc[1:4])
# new_df = df.iloc[1:3]
# print(new_df)
#
# print(df.loc[1,'email'])

# print(df['Country or region'].value_counts())
number = 0
while number < df.shape[0]:
    if df.loc[number,'GDP per capita'] > 1:
        print(df.loc[number,'Country or region'],df.loc[number, 'GDP per capita'])
    number += 1

