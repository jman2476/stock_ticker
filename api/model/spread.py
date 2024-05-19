from services.data_analyzer import get_latest_spread

class SpreadModel:
    def __init__(self):
        spread = get_latest_spread()

        self.time = spread['time']
        self.symbol = spread['symbol']
        self.finnhub = spread['finn_spread']
        self.twelve_data = spread['twelve_spread']
        self.yfinance = spread['yfin_spread']