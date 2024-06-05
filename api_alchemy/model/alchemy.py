# TODO: The purpose of this document is to serve as the basis for defining the models of the sdqlalchemy version of the stock quote API, including a PriceData model and a Company model

from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Float, TEXT, select
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class PriceData(Base):
    __tableName__ = 'price_quotes'

    time = Column('time', TEXT, primary_key=True)
    symbol = Column(TEXT, ForeignKey("company.symbol"))
    finnhub = Column('finnhub', Float)
    twelve_data = Column('twelve_data', Float)
    yfinance = Column('yfinance', Float)
    average = Column('average', Float)
    finn_spread = Column('finn_spread', Float)
    twelve_spread = Column('twelve_spread', Float)
    yfin_spread = Column('yfin_spread', Float)


    def __init__(self, time, symbol, finnhub, twelve_data, yfinance, average, finn_spread, twelve_spread, yfin_spread):
        self.time = time
        self.symbol = symbol
        self.finnhub = finnhub
        self.twelve_data = twelve_data
        self.yfinance = yfinance
        self.average = average
        self.finn_spread = finn_spread
        self.twelve_spread = twelve_spread
        self.yfin_spread = yfin_spread
    
    def __repr__(self):
        return f"T: {self.time} S: {self.symbol} Q: ({self.finnhub}, {self.twelve_data}, {self.yfinance}) M:{self.average} D: [{self.finn_spread}, {self.twelve_spread}, {self.yfin_spread}]"


class Company(Base):
    __tableName__ = 'price_quotes'

    symbol = Column('symbol', TEXT, primary_key=True)
    name = Column('name', TEXT)
    market_cap = Column('market_cap', Integer)
    volume = Column('volume', Integer)
    exchange = Column('exchange', TEXT)



    def __init__(self, symbol, name, market_cap, volume, exchange):
        self.symbol = symbol
        self.name = name
        self.market_cap = market_cap
        self.volume = volume
        self.exchange = exchange
    
    def __repr__(self):
        return f"{self.symbol}: {self.name}, money traded: {self.market_cap}, volume traded: {self.volume}, exchange: {self.exchange}"