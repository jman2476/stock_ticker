import requests
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