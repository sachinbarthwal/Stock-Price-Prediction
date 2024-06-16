import pandas as pd
import joblib

def predict_stock_price(stock_symbol, model_path):
    # Load your dataset
    df = pd.read_csv(f'data/{stock_symbol}.csv')
    
    # Assume we're using the last 5 closing prices as features to predict the next closing price
    input_features = df['Close'].tail(5).tolist()
    
    model = joblib.load(model_path)
    prediction = model.predict([input_features])
    return prediction
