# TODO: write the route functions to get the latest data from the database for quotes, average, spread, and company metadata
from connection.engine import Session
from model.alchemy import PriceData, Company
from sqlalchemy import select

# Retreive the stock  quotes from the database
def get_latest_quotes(session):
    quotes = {}
    try:
        quotes = session.execute(
            select(PriceData.time, PriceData.symbol, PriceData.finnhub, PriceData.twelve_data, PriceData.yfinance).order_by(PriceData.time.desc()).limit(1)
        )

        result = quotes.first()
        print('Results:', result)
    except Exception as err:
        print('Quotes got donked')
        print(err)
    return result._asdict()

# Retreive the stock average qutoe from the database
def get_latest_average(session):
    average = {}
    try:
        average = session.execute(
            select(PriceData.time, PriceData.symbol, PriceData.average).order_by(PriceData.time.desc()).limit(1)
        )
    except Exception as err:
        print(err)
    return average.first()._asdict()

# Retreive the stock spread from the database
def get_latest_spread(session):
    spread = {}
    try:
        spread = session.execute(
            select(PriceData.time, PriceData.symbol, PriceData.finn_spread, PriceData.twelve_spread, PriceData.yfin_spread).order_by(PriceData.time.desc()).limit(1)
        )
    except Exception as err:
        print(err)
    return spread.first()._asdict()

# Retreive the company metadata for the current stock ticker
def get_company_data(session):
    return