import yfinance as yf

def fetch_stock_data(stock_symbol, start_date, end_date):
    # Fetch data using yfinance
    data = yf.download(stock_symbol, start=start_date, end=end_date)
    # Save data to CSV
    data.to_csv(f'data/{stock_symbol}.csv')
    return data