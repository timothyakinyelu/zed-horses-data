from flask import Flask
from flask_cors import CORS
from settings.config import Config


def createApp():
    """ initiate the application """
    
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)
    CORS(app)

    with  app.app_context():
        # register blueprint
        from src.views.bet_view import bet as bet_blueprint
        app.register_blueprint(bet_blueprint)

        return app
