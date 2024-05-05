import finnhub
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

# Get quote from finnhub
quote_finnhub = finnhub_client.quote(ticker_symbol)
# Get quote from polygon
quotes_polygon = polygon_client.list_quotes(ticker=ticker_symbol, timestamp='2024-03-24')
# Get Quote from twelve data
quote_twelveData = twelveData_client.quote(symbol=ticker_symbol)

print("Finnhub: ", quote_finnhub)
print("Twelve Data: ", quote_twelveData.as_json())

# for quote in quotes_polygon:
#     print("Polygon: ", quote)