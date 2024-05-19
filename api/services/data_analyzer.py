# Get the latest information from the database, and analyze it before returning it
import sqlite3


def connect_to_db():
    con = sqlite3.connect('stock.db')
    return con

# Retreive the stock  quotes from the database
def get_latest_quotes():
    quotes = {}

    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute('''SELECT time, symbol, finnhub, twelve_data, yfinance FROM stock_quotes ORDER BY time DESC LIMIT 1''')

    row = cur.fetchone()
    print(row)

    # Convert row to dict
    quotes['time'] = row[0]
    quotes['symbol'] = row[1]
    quotes['finnhub'] = row[2]
    quotes['twelve_data'] = row[3]
    quotes['yfinance'] = row[4]

    conn.close()

    return quotes

# Retreive the stock average qutoe from the database
def get_latest_average():
    average = {}

    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute('''SELECT time, symbol, average FROM stock_quotes ORDER BY time DESC LIMIT 1''')

    row = cur.fetchone()
    print(row)

    # Convert row to dict
    average['time'] = row[0]
    average['symbol'] = row[1]
    average['average'] = row[2]

    conn.close()

    return average

# Retreive the stock spread from the database
def get_latest_spread():
    spread = {}

    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute('''SELECT time, symbol, finn_spread, twelve_spread, yfin_spread FROM stock_quotes ORDER BY time DESC LIMIT 1''')

    row = cur.fetchone()
    print(row)

    # Convert row to dict
    spread['time'] = row[0]
    spread['symbol'] = row[1]
    spread['finn_spread'] = row[2]
    spread['twelve_spread'] = row[3]
    spread['yfin_spread'] = row[4]

    conn.close()

    return spread

print(get_latest_quotes())
print(get_latest_average())
print(get_latest_spread())