import requests

def get_price_stock():
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=S&P500&interval=5min&apikey=9K8SDMA5M3YJEINP'
    r = requests.get(url)
    data = r.json()
    return data

# 9K8SDMA5M3YJEINP
print(get_price_stock())