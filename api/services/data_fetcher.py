# Fetches data from Finnhub, TwelveData, and yFinance
# Import financial data APIs
import finnhub
import yfinance as yf
from twelvedata import TDClient
# Import database tools
import sqlite3
from datetime import datetime

# Import helpers
from dotenv import dotenv_values
import asyncio
# Load environment variables
env_vars = dotenv_values('.env')

# Initialize API clients for Finnhub and Twelve Data
# yFinance will be initialized in its function
finnhub_client = finnhub.Client(api_key=env_vars['FINNHUB_API_KEY'])
twelveData_client = TDClient(apikey=env_vars['TWELVEDATA_API_KEY']) 

# DB connection function
def connect_to_db():
    con = sqlite3.connect('stock.db')
    return con

# counters to track how many times each has been used
finn_counter = 0
twelve_counter = 0
yfin_counter = 0

# Functions to fetch data from the APIs
# Finnhub fetch
async def get_finnhub(ticker_symbol):
    try: 
        data = await finnhub_client.quote(ticker_symbol)
        finn_counter = finn_counter + 1
        close_price = data['c']
        return close_price
    except:
        raise Exception('No data returned from finnhub')
    
# Twelve Data fetch
async def get_twelve_data(ticker_symbol):
    try:
        data = await twelveData_client.quote(symbol=ticker_symbol)
        twelve_counter = twelve_counter + 1
        close_price = float(data.as_json()['close'])
        return close_price
    except:
        raise Exception('No data returned from finnhub')

# yFinance fetch
async def get_yfinance(ticker_symbol):
    try:
        yf_ticker = await yf.Ticker(ticker_symbol)
        data = yf_ticker.history('1d')
        close_price = data.iloc[0]['Close']
        return close_price
    except:
        raise Exception('Unable to get data from yfinance')

# Averaging function, takes a dictionary as parameter
def average(quotes):
    mean = sum(quotes.values()) / len(quotes)
    return round(mean, 2)

# Slippage function
def slippage(quotes, mean):
    slip = {}

    for key in quotes.keys():
        quotes[key] = abs(quotes[key] - mean)
        slip[key] = round(quotes[key], 4)

    return slip

# Analysis function with parameters (finnhub, twelve data, yfinance)
def anaylizer(quote1, quote2, quote3):
    quotes = {
        "finnhub" : quote1,
        "twelve_data" : quote2,
        "yfinance" : quote3
    }
    mean = average(quotes)
    slip = slippage(quotes, mean)

    return (quotes, mean, slip)

# Database writer
def insert_entry(ticker_symbol, quotes, mean, slippage):
    inserted_row = {}
    try: 
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute('''
                    INSERT INTO stock_quotes 
                    (time, symbol, finnhub, twelve_data, yfinance, average, finn_spread, twelve_spread, yfin_spread)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                     (datetime.datetime, ticker_symbol, quotes['finnhub'], quotes['twelve_data'], quotes['yfinance'], mean, slippage['finnhub'], slippage['twelve_data'], slippage['yfinance']))
        
        conn.commit()

    except:
        conn.rollback()

    finally:
        conn.close()

    return inserted_row


def get_latest_entry():
    last_entry = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute('''
            SELECT 
                time, symbol, finnhub, twelve_data, yfinance, average, finn_spread, twelve_spread, yfin_spread
                LAST_VALUE (time)
            FROM stock_quotes
            ''')
        row = cur.fetchone()

        # Convert row into last_entry dict
        last_entry['time'] = row['time']
        last_entry['symbol'] = row['symbol']
        last_entry['finnhub'] = row['finnhub']
        last_entry['twelve_data'] = row['twelve_data']
        last_entry['yfinance'] = row['yfinance']
        last_entry['average'] = row['average']
        last_entry['finn_spread'] = row['finn_spread']
        last_entry['time'] = row['time']
        last_entry['time'] = row['time']

    except:
        last_entry = {}
    finally:
        conn.close()

    return last_entry

# Check if trading hours are active
def trading_hours_check(time_object):
    print(time_object.hour)
    if (time_object.weekday() > 5): return False
    if (time_object.hour < 9 or time_object.hour > 5): return False

    return True


# Timer function: Updates the database every 15s
# if an API limit is reached, return error for specific API
# Verify the time is during trading hours;
#       9a-5p EST Mon-Fri
# Important!!!!! This function cannot be directly reading the desired ticker symbol! You must pass in the value from the user
async def up_data_base(ticker_symbol, counter = 0):

    timestamp = datetime.today()
    print(timestamp, isinstance(timestamp, datetime))
    if (not trading_hours_check(timestamp)):
        finn = await get_finnhub(ticker_symbol)
        twelve = await get_twelve_data(ticker_symbol)
        yfin = await get_yfinance(ticker_symbol)
        
        data = anaylizer(finn, twelve, yfin)        

        insert_entry(ticker_symbol, data[0], data[1], data[2])

        print(get_latest_entry())
        # Lets get recursive and call ourselves every 15 seconds
        counter += 1
        await asyncio.sleep(15)
        if (counter < 20):
            up_data_base(ticker_symbol, counter)
                        
asyncio.run(up_data_base('AAPL'))