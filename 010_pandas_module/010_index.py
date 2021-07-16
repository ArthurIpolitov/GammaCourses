import pandas as pd
df = pd.read_csv('2019.csv')
# DATA FRAME
# df = pd.read_csv('2019.csv') # DATA FRAME
# print(df)

# ITER ROWS
# df = pd.read_csv('2019.csv')
# for index, row in df.iterrows():
#     print(index)
#     print(row['Country or region'])

#LOC AND INLOC

# print(df.loc[df['Country or region'] == 'Estonia'])

# SHAPE AND DESCRIBE

# print(df.shape)
# print(df.describe())
# print(df.loc[0, 'GDP per capita'])

# SORT VALUES

# print(df.sort_values('Country or region'))

# MAKE AND DROP TABLES

# df['Total'] = df['GDP per capita'] + df['Generosity'] + df['Social support']
# df = df.drop(columns=['Total'])
# print(df)

# STR AND LOC
# print(df.loc[df['Country or region'].str.contains('est')])

# WHERE
# s = pd.Series(range(5))
# print(s.where(s > 0, 'I N V A L I D'))

# print(df.sort_values(by='Generosity'))
