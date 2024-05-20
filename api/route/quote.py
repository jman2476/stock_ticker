from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from
from model.quotes import QuoteModel
from schema.quotes import QuotesSchema
from model.average import AverageModel
from schema.average import AverageSchema
from model.spread import SpreadModel
from schema.spread import SpreadSchema

stock_quote_api = Blueprint('api', __name__)


@stock_quote_api.route('/quotes')
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
    result = QuoteModel()
    return QuotesSchema().dump(result), 200


@stock_quote_api.route('/average')
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

    result = AverageModel()
    return AverageSchema().dump(result), 200


@stock_quote_api.route('/spread')
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

    result = SpreadModel()
    return SpreadSchema().dump(result), 200