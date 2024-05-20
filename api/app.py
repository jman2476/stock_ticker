from flask import Flask
from flasgger import Swagger
from route.quote import stock_quote_api
#from services.data_fetcher import up_data_base
import asyncio

def create_app():
    app = Flask(__name__)
    
    app.config['SWAGGER'] = {
        'title': 'Stock Statistics API',
    }
    swagger = Swagger(app)
     ## Initialize Config
    app.config.from_pyfile('config.py')
    app.register_blueprint(stock_quote_api, url_prefix='/api')

    return app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen to, not starboard')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(port=port)

