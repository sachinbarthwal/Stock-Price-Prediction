import os
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

def train_model(stock_symbol):
    df = pd.read_csv(f'data/{stock_symbol}.csv')
    X = df.drop(['Close', 'Date'], axis=1)  # Features (all columns except 'Close') Exclude 'Date' column as well
    y = df['Close']  # Target variable (the 'Close' column)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Ensure 'models' directory exists
    models_dir = 'models'
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)

    # Save the trained model to a file
    model_path = f'{models_dir}/{stock_symbol}_model.joblib'
    joblib.dump(model, model_path)
    
    return model_path  # Return the path where the model is saved
