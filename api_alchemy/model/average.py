from services.data_fetcher import get_latest_average

class AverageModel:
    def __init__(self, session):
        average = get_latest_average(session)

        self.time = average['time']
        self.symbol = average['symbol']
        self.average = average['average']