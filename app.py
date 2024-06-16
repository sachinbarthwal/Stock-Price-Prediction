from flask import Flask, request, render_template
import datetime
import pandas as pd
from src.data_fetcher import fetch_stock_data
from src.model import train_model
from src.predict import predict_stock_price
from src.visualize import plot_results

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    actual_prices = []
    predicted_prices = []
    
    if request.method == 'POST':
        stock_name = request.form['stock_name']
        start_date_str = (datetime.datetime.now() - datetime.timedelta(days=365)).strftime('%Y-%m-%d')
        end_date_str = datetime.datetime.now().strftime('%Y-%m-%d')
        
        fetch_stock_data(stock_name, start_date_str, end_date_str)
        model_path = train_model(stock_name)
        
        prediction = predict_stock_price(stock_name, model_path)[0]
        
        df = pd.read_csv(f'data/{stock_name}.csv')
        actual_prices = df['Close'].tail(5).tolist()
        predicted_prices.append(prediction)
        
        plot_results(stock_name, actual_prices, predicted_prices)
        
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
