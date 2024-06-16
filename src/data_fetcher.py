import pandas_datareader as web
import datetime

def fetch_stock_data(stock_symbol, start_date, end_date):
    df = web.DataReader(stock_symbol, 'yahoo', start_date, end_date)
    df.to_csv(f'data/{stock_symbol}.csv')
    return df

if __name__ == "__main__":
    fetch_stock_data('AAPL', datetime.datetime(2020, 1, 1), datetime.datetime(2021, 1, 1))
