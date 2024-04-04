from flask import Flask
from config import Config
import sys
import logging


# Flask application factory function.
def create_app(config_class=Config):
    # Setup logging and handlers
    logging.getLogger().handlers.clear()
    formatter = logging.Formatter('%(asctime)s %(levelname)s Flask %(message)s')
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    logging.getLogger().addHandler(handler)
    logging.getLogger().setLevel(logging.INFO)

    # Flask app instance
    logging.info("Initializing Flask application.")
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app

