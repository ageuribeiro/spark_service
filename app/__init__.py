from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
import logging
from ..logging_config import logger, save_log_json

db = SQLAlchemy()

mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client['logs']

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    from .controllers import register_controllers
    register_controllers(app)

    logger.debug("Application running...")
    return app