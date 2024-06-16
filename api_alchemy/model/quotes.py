from services.data_fetcher import get_latest_quotes

class QuoteModel:
    def __init__(self, session):
        print('Session: ', session)
        quotes = get_latest_quotes(session)
        print(quotes)

        self.time = quotes['time']
        self.symbol = quotes['symbol']
        self.finnhub = quotes['finnhub']
        self.twelve_data = quotes['twelve_data']
        self.yfinance = quotes['yfinance']