# Gathers and analyzes data from Finnhub, TwelveData, and yFinance

#import financial data APIs
import finnhub
import yfinance as yf
from twelvedata import TDClient
# Import SQLAlchemy session factory, classes, helpers and tools
from connection.engine import Session 
from model.alchemy import PriceData, Company
from datetime import datetime
from dotenv import dotenv_values
import os
# Load environment variables
env_vars = dotenv_values('.env')

# Function to get environment variables
def get_vars(key_name):
    try:
        print('var1')
        print('var2: ', env_vars)
        return env_vars[key_name]
    except Exception as e:
        print('Vars error: ', e)
        return Exception('Issue getting variables')

# Functions to fetch data from the APIs
# Finnhub fetch
def get_finnhub(ticker_symbol):
    print('finn')
    try: 
        finnhub_client = finnhub.Client(api_key=os.environ['FINNHUB_API_KEY'])
        print('Finn client: ', finnhub_client)
        data = finnhub_client.quote(ticker_symbol)
        print("Finnhub: ", data)
        close_price = data['c']
        return close_price
    except Exception as e:
        print('finnhub error:', e)
        return Exception('No data returned from finnhub')

# Twelve Data fetch
# TODO: also fetch and return metadata from Twelve Data
def get_twelve_data(ticker_symbol, session):
    print('twelve')
    try:
        twelveData_client = TDClient(apikey=os.environ['TWELVEDATA_API_KEY']) 
        data = twelveData_client.quote(symbol=ticker_symbol)
        close_price = float(data.as_json()['close'])
        print('Twelve: ', data.as_json())
        set_company_data(data, session)
        return close_price
    except Exception as e:
        print('twelve error:', e)
        return Exception('No data returned from twelve data')

# yFinance fetch
def get_yfinance(ticker_symbol):
    print('yfi')
    try:
        yf_ticker = yf.Ticker(ticker_symbol)
        data = yf_ticker.history('1d')
        close_price = data.iloc[0]['Close']
        print('yFinance: ', data)
        return close_price
    except Exception as e:
        print('yfinnance error: ', e)
        return Exception('Unable to get data from yfinance')
    
# Extract company data from Twelve Data client information
def set_company_data(data, session):
    try:
        new_company = Company(data.as_json()['symbol'], data.as_json()['name'], data.as_json()['currency'], data.as_json()['volume'], data.as_json()['exchange'])

        print('new company: ', new_company)
        session.add(new_company)
        session.commit()

    except Exception as err:
        print('Company data error:', err)
    return 

# Averaging function, takes a dictionary as parameter
def average(quotes):
    print(quotes)
    mean = sum(quotes.values()) / len(quotes)
    print('average2')

    return round(mean, 2)

# Slippage function
def slippage(quotes, mean):
    print('slip')
    slip = {}
    dummy_quotes = quotes.copy()
    for key in quotes.keys():
        dummy_quotes[key] = abs(quotes[key] - mean)
        slip[key] = round(dummy_quotes[key], 4)

    return slip

# Analysis function with parameters (finnhub, twelve data, yfinance)
def analyzer(quote1, quote2, quote3):
    quotes = {
        "finnhub" : quote1, 
        "twelve_data" : quote2,
        "yfinance" : quote3
    }
    mean = average(quotes)
    slip = slippage(quotes, mean)
    
    return (quotes, mean, slip)

# Database writer
# TODO: refactor old insert_entry code into SQLAlchemy code
def insert_entry(timestamp, ticker_symbol, quotes, mean, slippage, session):
    try:
        new_price = PriceData(timestamp, ticker_symbol, quotes['finnhub'], quotes['twelve_data'], quotes['yfinance'], mean, slippage['finnhub'], slippage['twelve_data'], slippage['yfinance'])

        session.add(new_price)
        session.commit()

    except Exception as err:
        print(err)
        
    return new_price

# Fetch most recent entry
# TODO: refactor old get_latest_entry code into SQLAlchemy code
def get_latest_entry(session):
    last_entry = {}
    try:
        last_entry = session.query(PriceData).order_by(PriceData.time.desc())
        session.execute
    except Exception as err:
        print(err)
    
    return last_entry

# Check if trading hours are active
def trading_hours_check(time_object):
    print(time_object.hour)
    print(time_object.weekday())
    if (time_object.weekday() > 5): return False
    if (time_object.hour < 9 or time_object.hour > 17): return False

    return True

# Gather all necessary information (quotes, average, spread) and update the quotes database
def up_data_base(ticker_symbol, session):
    timestamp = datetime.today()
    print(timestamp, isinstance(timestamp, datetime))
    if (trading_hours_check(timestamp)):
        print('cheese')
        finn = get_finnhub(ticker_symbol)
        twelve = get_twelve_data(ticker_symbol, session)
        yfin = get_yfinance(ticker_symbol)
        
        data = analyzer(finn, twelve, yfin)        

        insert_entry(timestamp, ticker_symbol, data[0], data[1], data[2], session)

        print(get_latest_entry(session))

