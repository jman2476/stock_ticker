from services.data_analyzer import get_latest_average

class AverageModel:
    def __init__(self):
        average = get_latest_average()

        self.time = average['time']
        self.symbol = average['symbol']
        self.average = average['average']