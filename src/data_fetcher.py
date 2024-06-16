import yfinance as yf

def fetch_stock_data(stock_symbol, start_date, end_date):
    # Fetch data using yfinance
    data = yf.download(stock_symbol, start=start_date, end=end_date)
    # Save data to CSV
    data.to_csv(f'data/{stock_symbol}.csv')
    return data

if __name__ == "__main__":
    # Fetch Apple's stock data from Jan 1, 2020, to Jan 1, 2021
    fetch_stock_data('HDFCBANK.NS', '2019-01-01', '2024-06-16')