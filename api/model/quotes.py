from services.data_analyzer import get_latest_quotes

class QuoteModel:
    def __init__(self):
        quotes = get_latest_quotes()

        self.time = quotes['time']
        self.symbol = quotes['symbol']
        self.finnhub = quotes['finnhub']
        self.twelve_data = quotes['twelve_data']
        self.yfinance = quotes['yfinance']