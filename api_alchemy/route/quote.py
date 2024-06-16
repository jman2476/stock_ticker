from http import HTTPStatus
from flask import Blueprint, request
from flasgger import swag_from
from model.quotes import QuoteModel
from schema.quotes import QuotesSchema
from model.average import AverageModel
from schema.average import AverageSchema
from model.spread import SpreadModel
from schema.spread import SpreadSchema
from model.symbol import SymbolModel
from schema.symbol import SymbolSchema
from connection.engine import Session


from services.data_analyzer import up_data_base, get_yfinance

stock_quote_api = Blueprint('api', __name__)

# TODO: write the post route for the ticker symbol
@stock_quote_api.post('/symbol')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Set the new ticker symbol',
            'schema': SymbolSchema
        },
        HTTPStatus.BAD_REQUEST.value: {
            'description': 'Please provide a valid stock ticker symbol LMAO',
            'schema': SymbolSchema
        }
    }
})
def post_ticker():
    """
    Posts the new ticker symbol 
    ---
    """
    result = SymbolModel()
    try:
    # Check that the ticker symbol provided actually exists 
        print(request.json['symbol'])
        ticker_symbol = request.json['symbol']
        quote = get_yfinance(ticker_symbol)
        print(quote)
        if (quote.__eq__('Unable to get data from yfinance')):
            result.message = 'Please provide a valid stock ticker symbol.'
            return SymbolSchema().dump(result), 404
        with Session() as session:
            up_data_base(ticker_symbol, session)
        result.message = 'Successfully updated ticker symbol'
        
        return SymbolSchema().dump(result), 200
    except:
        print(Exception('Post Ticker got donked up'))
        result.message = 'The API may be overcalled, or there could be an issue with the ticker symbol.'
        return SymbolSchema().dump(result), 404


@stock_quote_api.get('/quotes')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get multiple quotes of a stock',
            'schema': QuotesSchema
        }
    }
})
def get_quotes():
    """
    returns Twelve Data, Finnhub and yFinance quotes

    ---
    """
    with Session() as session:
        result = QuoteModel(session)
    return QuotesSchema().dump(result), 200


@stock_quote_api.get('/average')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get average of 3 stock quotes',
            'schema': AverageSchema
        }
    }
})
def get_average(): 
    """
    returns averages

    ---
    """
    with Session() as session:
        result = AverageModel(session)
    return AverageSchema().dump(result), 200


@stock_quote_api.get('/spread')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get the differenect between the average and the quote price for each source',
            # 'schema': SpreadSchema
        }
    }
})
def get_spread():
    """
    returns Twelve Data, Finnhub and yFinance spreads

    ---
    """
    with Session() as session:
        result = SpreadModel(session)
    return SpreadSchema().dump(result), 200