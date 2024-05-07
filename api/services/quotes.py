import finnhub
import yfinance as yf
from polygon import RESTClient
from twelvedata import TDClient

from dotenv import dotenv_values

# load values from .env file
env_vars = dotenv_values('.env')

# set api keys to variables
finnhub_key = env_vars['FINNHUB_API_KEY']
polygon_key = env_vars['POLYGON_API_KEY']
twelveData_key = env_vars['TWELVEDATA_API_KEY']


# Set up/initialize clients for each API
finnhub_client = finnhub.Client(api_key=finnhub_key) 
# 30 calls/min API Limit
polygon_client = RESTClient(api_key=polygon_key) 
# 5 calls/min API Limit
twelveData_client = TDClient(apikey=twelveData_key) 
# 8 calls/min and 800 calls/day API Limit

ticker_symbol = 'AAPL'

# Set up yfinance stock ticker
yf_ticker = yf.Ticker(ticker_symbol)

# Get quote from finnhub
quote_finnhub = finnhub_client.quote(ticker_symbol)
# Get quote from polygon
quotes_polygon = polygon_client.list_quotes(ticker=ticker_symbol, timestamp='2024-03-24')
# Get Quote from twelve data
quote_twelveData = twelveData_client.quote(symbol=ticker_symbol)
# Get quote from yfinance
quote_yfinance = yf_ticker.history(period="1d")

# print("Finnhub: ", quote_finnhub["c"], quote_finnhub)
# print("Twelve Data: ", quote_twelveData.as_json()['close'], quote_twelveData.as_json())
# print("yFinance: ", quote_yfinance.iloc[0]['Close'], quote_yfinance)

# function to return an list of quotes for a given stock
def quotes(ticker_symbol):

    return {
        "finnhub" : quote_finnhub["c"],
        "twelve_data" : float(quote_twelveData.as_json()['close']),
        "yfinance" : quote_yfinance.iloc[0]['Close']
    }

# function to find the average of all stock quotes
def average():
    prices = quotes('AAPL')
    mean = sum(prices.values()) / 3

    return round(mean, 2)

# function to find the difference between each quote and the average price
def slippage():
    mean = average()
    prices = quotes('AAPL')
    slippage = {}

    for key in prices.keys():
        prices[key] = abs(prices[key] - mean)
        slippage[key] = round(prices[key], 4)

    return slippage

print(quotes('AAPL'))
print(average())
print(slippage())