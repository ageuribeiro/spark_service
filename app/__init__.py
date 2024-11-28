from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
from config import Config
import logging
from log_config import logger, save_log_json

db = SQLAlchemy()

client = MongoClient("mongodb://localhost:27017/")
mongo_db = client.get_database('spark_db')
logs_collection = mongo_db.get_collection('logs')
# mongo_db = client['logs']

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.config["MONGO_CLIENT"] = client
    app.config["LOGS_COLLECTION"] = logs_collection

    db.init_app(app)

    from .controllers import register_controllers
    register_controllers(app)

    from app.views.views import main_bp
    app.register_blueprint(main_bp)

    logger.debug("Application running...")

    return app