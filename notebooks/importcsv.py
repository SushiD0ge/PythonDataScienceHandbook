import pandas as pd

# csv or excel
data = pd.read_csv('data/Tutorial.csv')
data = pd.ExcelFile('data/Tutorial.xlsx')

# make pivot table
df = data.parse()
data = data.parse()
# for data
data = data.pivot_table(index='Year',aggfunc={'Units_sold':sum})
# for df
df.pivot_table(index=['Year','Quarter']
,aggfunc={'Units_sold':sum})
# make filter for table
df = df.query('Quarter == "Q3"')
df = df.pivot_table(index=['Year'])
df.columns = ['Q3']

# marge the tables
output = data.join(df)

# make filter for table
# sample
# mu = quartiles[1]
# sig = 0.74 * (quartiles[2] - quartiles[0])
# df = df.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')
# df = df.query('Quarter == "Q3"')

# output as csv
output.to_csv('BT.csv')