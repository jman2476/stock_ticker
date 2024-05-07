from flask_marshmallow import Schema
from marshmallow.fields import Str


class QuotesSchema(Schema):
    class Meta: 
        # Fields to expose
        fields = ["TW_quote","Finn_quote"]

    TW_quote = Str()
    Finn_quote = Str()