import cbpro
import pandas as pd
import datetime

c = cbpro.PublicClient()

all_products = c.get_products()
print(all_products[0:3])

usd_products = []
tradable_products = []
not_tradable_products = []
for product in all_products:
    id_output = product.get('id')
    if "USD" == id_output[-3:]:
        usd_products.append(id_output)
        trade_disabled = product.get("trading_disabled")
        if trade_disabled:
            not_tradable_products.append(id_output)
        elif trade_disabled == False:
            tradable_products.append(id_output)

print("tradable products")
print(tradable_products)
print("------------------------------------------")

print("not tradable products")
print(not_tradable_products)
print("------------------------------------------")


def pull_all_daily_data(ticker):
    
    end_date = datetime.date(2021, 11, 6)
    delta_300 = datetime.timedelta(300)
    delta_1 = datetime.timedelta(1)

    return_length = 1
    first_period = True
    output_data = pd.DataFrame()

    while return_length > 0:
        if first_period:
            start_date = end_date - delta_300
            first_period = False
            
        else:
            end_date = start_date
            start_date = start_date - delta_300

        data_pull = c.get_product_historic_rates(product_id = ticker, granularity = 86400, start = start_date.isoformat(), end = end_date.isoformat())
        output_data = output_data.append(data_pull)
        return_length = len(data_pull)

    output_data.columns= ["Date","Open","High","Low","Close","Volume"]
    output_data['Date'] = pd.to_datetime(output_data['Date'], unit='s')
    return output_data

for ticker_input in usd_products:
    print(ticker_input)
    if ticker_input == "UMA-USD":
        continue
    daily_data_df = pull_all_daily_data(ticker = ticker_input)
    daily_data_df.to_csv("./daily_data/" + ticker_input + "_daily_data.csv")

