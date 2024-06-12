from services.data_fetcher import get_latest_spread

class SpreadModel:
    def __init__(self, session):
        spread = get_latest_spread(session)

        self.time = spread['time']
        self.symbol = spread['symbol']
        self.finnhub = spread['finn_spread']
        self.twelve_data = spread['twelve_spread']
        self.yfinance = spread['yfin_spread']