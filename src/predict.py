import joblib

def predict_stock_price(model_path, input_features):
    model = joblib.load(model_path)
    prediction = model.predict([input_features])
    return prediction

if __name__ == "__main__":
    print(predict_stock_price('model.joblib', [/* input features */]))
