from flask_marshmallow import Schema
from marshmallow.fields import Str, Float

class SpreadSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ['time', 'symbol', 'finnhub', 'twelve_data', 'yfinance']

    time = Str()
    symbol = Str()
    finnhub = Float()
    twelve_data = Float()
    yfinance = Float()