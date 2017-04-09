import pandas as pd

# csv or excel
data = pd.read_csv('data/result_fx.csv')

# make pivot table
data = data.parse()
# for data
sell = data.query('type == "sell"')
sell.merge(sell, data['profit'], on="order_num")
buy = data.query('type == "buy"')

# connect close


data = data.pivot_table(index='Year',aggfunc={'Units_sold':sum})
# for df
df.pivot_table(index=['Year','Quarter']
,aggfunc={'Units_sold':sum})
# make filter for table
df = df.query('Quarter == "buy"')
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