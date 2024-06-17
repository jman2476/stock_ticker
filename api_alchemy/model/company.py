from services.data_fetcher import get_company_data

class CompanyModel: 
    def __init__(self, session):
        company = get_company_data(session)

        self.symbol = company['symbol']
        self.name = company['name']
        self.currency = company['currency']
        self.volume = company['volume']
        self.exchange = company['exchange']