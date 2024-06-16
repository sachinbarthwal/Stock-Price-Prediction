import matplotlib.pyplot as plt

def plot_results(actual_prices, predicted_prices):
    plt.figure(figsize=(10,5))
    plt.plot(actual_prices, label='Actual Prices')
    plt.plot(predicted_prices, label='Predicted Prices')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_results([/* actual prices */], [/* predicted prices */])
