from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from
from model.quotes import QuoteModel
from schema.quotes import QuotesSchema

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
    #TODO: write the function to handle this route
    """
    returns Twelve Data and Finnhub quotes

    ---
    """
    result = QuoteModel()
    return QuotesSchema().dump(result), 200


@stock_quote_api.route('/average')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get average of 3 stock quotes',
            # 'schema': AverageSchema
        }
    }
})
def get_average():
    #TODO: write function to handle averages route
    return "Work in progress"


@stock_quote_api.route('/slippage')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get the differenect between the average and the quote price for each source',
            # 'schema': SlippageSchema
        }
    }
})
def get_slippage():
    #TODO: write function to handle the slippage route
    return "Work in progress"