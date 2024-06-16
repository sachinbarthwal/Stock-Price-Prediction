import pandas as pd
import joblib

# Load your dataset
df = pd.read_csv('data/HDFCBANK.NS.csv')

# Assume we're using the last 5 closing prices as features to predict the next closing price
input_features = df['Close'].tail(5).tolist()

def predict_stock_price(model_path, input_features):
    model = joblib.load(model_path)
    prediction = model.predict([input_features])
    return prediction

if __name__ == "__main__":
    print(predict_stock_price('model.joblib', input_features))