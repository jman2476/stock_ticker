from flask_marshmallow import Schema
from marshmallow.fields import Str, Float

class AverageSchema(Schema):
    class Meta:
        #Fields to expose
        fields = ['time', 'symbol', 'average']

    time = Str()
    symbol = Str()
    average = Float()