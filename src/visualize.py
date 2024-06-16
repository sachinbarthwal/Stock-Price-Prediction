import matplotlib.pyplot as plt
import pandas as pd

def plot_results(stock_symbol, actual_prices, predicted_prices):
    # Ensure predicted_prices is a list with the same length as actual_prices
    predicted_prices = [predicted_prices[0]] * len(actual_prices)
    
    dates = pd.date_range(start=pd.to_datetime('today') - pd.Timedelta(days=len(actual_prices) - 1), periods=len(actual_prices), freq='D')
    
    plt.figure(figsize=(10,5))
    plt.plot(dates, actual_prices, label='Actual Prices', marker='o')
    plt.plot(dates, predicted_prices, label='Predicted Prices', linestyle='--', marker='x')
    plt.legend()
    plt.title(f'Stock Price Prediction for {stock_symbol}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True)
    plt.show()
