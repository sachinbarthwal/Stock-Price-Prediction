import matplotlib.pyplot as plt
import pandas as pd
import joblib

# Load your dataset
df = pd.read_csv('data/HDFCBANK.NS.csv')

# Assume we're using the last 5 closing prices as features to predict the next closing price
# And we have 5 days of predictions
input_features = df['Close'].tail(5).tolist()
actual_prices = df['Close'].tail(5).tolist()  # This should be the actual prices you want to compare

# Load your trained model
model = joblib.load('model.joblib')

# Make predictions
predicted_prices = []
for i in range(5):  # Assuming we're making 5 predictions
    input_feature = df['Close'].iloc[-(5+i):-i].tolist() if i > 0 else input_features
    predicted_price = model.predict([input_feature])
    predicted_prices.append(predicted_price[0])

def plot_results(actual_prices, predicted_prices):
    plt.figure(figsize=(10,5))
    plt.plot(actual_prices, label='Actual Prices')
    plt.plot(predicted_prices, label='Predicted Prices')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_results(actual_prices, predicted_prices)