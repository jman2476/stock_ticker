from flask_marshmallow import Schema
from marshmallow.fields import Str

class SymbolSchema(Schema):
    class Meta:
        fields = ['message']

    message = Str()