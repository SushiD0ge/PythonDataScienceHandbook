import pandas as pd

# csv or excel
data = pd.read_csv('data/result_fx.csv')

# filter
# sell
sell = data.query('type == "sell"')
sell_num = sell['order_num']
sell_num = sell_num.to_frame().reset_index()
sell_list = data.merge(sell_num)
# buy
buy = data.query('type == "buy"')
buy_num = buy['order_num']
buy_num = buy_num.to_frame().reset_index()
buy_list = data.merge(buy_num)

# output as csv
sell_list.to_csv('sell_list.csv')
buy_list.to_csv('buy_list.csv')