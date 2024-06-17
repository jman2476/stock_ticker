from flask_marshmallow import Schema
from marshmallow.fields import Str, Float, Int

class CompanySchema(Schema):
    class Meta: 
        # Fields to expose
        fields = ['symbol', 'name', 'currency', 'volume', 'exchange']

    symbol = Str()
    name = Str()
    currency = Str()
    volume = Int()
    exchange = Str()