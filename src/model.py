from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import joblib

def train_model(stock_symbol):
    df = pd.read_csv(f'data/{stock_symbol}.csv')
    X = df.drop(['Close', 'Date'], axis=1)  # Features (all columns except 'Close') Exclude 'Date' column as well
    y = df['Close']  # Target variable (the 'Close' column)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = LinearRegression()
    model.fit(X_train, y_train)
    # Save the trained model to a file
    joblib.dump(model, 'model.joblib')
    return model

if __name__ == "__main__":
    train_model('HDFCBANK.NS')