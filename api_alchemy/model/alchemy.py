# TODO: The purpose of this document is to serve as the basis for defining the models of the sdqlalchemy version of the stock quote API, including a PriceData model and a Company model

from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Float, TEXT, select
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class PriceData(Base):
    __tablename__ = 'price_quotes'
    

    time = Column('time', TEXT, primary_key=True)
    # symbol = Column(TEXT, ForeignKey("company.symbol"))
    company = Column()
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
    __tablename__ = 'company'
    # __table_args__ = {'extend_existing': True}

    name = Column('name', TEXT, primary_key=True)
    symbol = Column('symbol', TEXT)
    currency = Column('currency', TEXT)
    volume = Column('volume', Integer)
    exchange = Column('exchange', TEXT)
    # Columns to add: exchange time zone


    def __init__(self, symbol, name, currency, volume, exchange):
        self.symbol = symbol
        self.name = name
        self.currency = currency
        self.volume = volume
        self.exchange = exchange
    
    def __repr__(self):
        return f"{self.symbol}: {self.name}, money traded: {self.currency}, volume traded: {self.volume}, exchange: {self.exchange}"
