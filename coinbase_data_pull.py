import cbpro
import pandas as pd
import numpy as np
import datetime

c = cbpro.PublicClient()

all_products = c.get_products()
usd_products = []

# Get all USD tradable products
for product in all_products:
    id_output = product.get('id')
    if "USD" == id_output[-3:]:
        usd_products.append(id_output)

# Fuction to pull data for one pair
def pull_all_daily_data(ticker):
    
    end_date = datetime.date(2021, 12, 20)
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

# Loop over all identified USD pairs and pull dialy price data
for ticker_input in usd_products:
    print(ticker_input)
    
    # Skipping some tickers because they do not pull data but show up in the products we pulled ealier
    try:
        # Write out daily data
        daily_data_df = pull_all_daily_data(ticker = ticker_input)
        daily_data_df.to_csv("./daily_data/" + ticker_input + "_dec_21_2021_daily_data.csv")
    except:
        print("BAD TICKER:  " + ticker_input)

