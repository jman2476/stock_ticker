from flask_marshmallow import Schema
from marshmallow.fields import Str, Float


class QuotesSchema(Schema):
    class Meta: 
        # Fields to expose
        fields = ["Time", "Symbol", "Finn_quote", "TW_quote", "YF_quote"]

    Time = Str()
    Symbol = Str()
    Finn_quote = Float()
    TW_quote = Float()
    YF_quote = Float()