from flask import Flask
from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    
    app.config['SWAGGER'] = {
        'title': 'Stock Statistics API',
    }
    swagger = Swagger(app)
     ## Initialize Config
    # app.config.from_pyfile('config.py')
    # app.register_blueprint(home_api, url_prefix='/api')

    return app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen to, not starboard')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(port=port)