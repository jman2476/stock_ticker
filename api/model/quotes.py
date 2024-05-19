from services.data_analyzer import get_latest_quotes

class QuoteModel:
    def __init__(self):
        quotes = get_latest_quotes()

        self.Time = quotes['time']
        self.Symbol = quotes['symbol']
        self.Finn_quote = quotes['finnhub']
        self.TW_quote = quotes['twelve_data']
        self.YF_quote = quotes['yfinance']