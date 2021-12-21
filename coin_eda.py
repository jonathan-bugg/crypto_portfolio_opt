import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join

file_list = listdir('./daily_data')
file_list_sub = file_list[0:2]

first = True
for file in file_list:
    coin_name = file.split("-")[0]
    if first:
        price_df = pd.read_csv('./daily_data/' + file)
        price_df['coin'] = coin_name
        first = False
    else:
        new_df = pd.read_csv('./daily_data/' + file)
        new_df['coin'] = coin_name
        price_df = price_df.append(new_df)

price_df = price_df.drop('Unnamed: 0', 1)


length_of_listing = price_df[['coin', 'Date']].groupby(by = 'coin').count()
length_of_listing = length_of_listing.nlargest(10, 'Date')

coins_to_trade = length_of_listing.index.to_list()

price_df = price_df[price_df['coin'].isin(coins_to_trade)]
price_df['Date'] = pd.to_datetime(price_df['Date'])
price_df_open = price_df[['Date', 'coin', 'Close']]
price_df_open = price_df.drop_duplicates()

price_df_long = price_df_open.pivot(index = 'Date', columns = 'coin', values = 'Close').dropna()

returns = price_df_long.pct_change()

for coin in coins_to_trade[0:2]:
    print(coin)
    returns_series = returns[coin] + 1
    print(np.prod(returns_series) - 1)

print((price_df_long.iloc[-1] - price_df_long.iloc[0])/price_df_long.iloc[0])
exit()
print(np.sum(returns.mean()))
print(returns)