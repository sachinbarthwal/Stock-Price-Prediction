from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

def train_model(stock_symbol):
    df = pd.read_csv(f'data/{stock_symbol}.csv')
    # Preprocess data and split into features (X) and target (y)
    # ...
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

if __name__ == "__main__":
    train_model('AAPL')
