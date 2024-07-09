import requests

API_KEY = 'ELJKZZOFMT4AQTDF'
BASE_URL = 'https://www.alphavantage.co/query'

def get_stock_price(symbol):
    response = requests.get(f"{BASE_URL}?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={API_KEY}")
    data = response.json()

    if 'Time Series (5min)' in data:
        latest_time = sorted(data['Time Series (5min)'].keys())[0]
        latest_price = data['Time Series (5min)'][latest_time]['4. close']
        return float(latest_price)
    else:
        # Handle the case where the API response does not contain the expected data
        return None