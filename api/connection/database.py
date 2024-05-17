import sqlite3

def connect_to_db():
    con = sqlite3.connect('stock.db')
    return con

con = connect_to_db()
cur = con.cursor()

# Create a table
cur.execute('''
    CREATE TABLE IF NOT EXISTS stock_quotes (
            time TEXT NOT NULL,
            symbol TEXT NOT NULL,
            finnhub FLOAT,
            twelve_data FLOAT,
            yfinance FLOAT,
            average FLOAT,
            finn_spread FLOAT,
            twelve_spread FLOAT,
            yfin_spread FLOAT
    )
    ''')
cur.execute('CREATE TABLE IF NOT EXISTS tests (name TEXT, numb INT, frac FLOAT)')
con.commit()

# Close the connection
cur.close()
con.close()

