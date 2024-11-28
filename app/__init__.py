from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
from config import Config
import logging
import os
from log_config import logger, save_log_json

db = SQLAlchemy()

client = MongoClient(os.environ.get("MONGO_URI"))
mongo_db = client.get_database('spark_db')
logs_collection = mongo_db.get_collection('logs')


def create_app():
    app = Flask(__name__, template_folder='views/templates')
    app.config.from_object('config.Config')
    app.config["MONGO_CLIENT"] = client
    app.config["LOGS_COLLECTION"] = logs_collection

    db.init_app(app)

    from .controllers import register_controllers
    register_controllers(app)

    from app.views.general_views import general_bp
    app.register_blueprint(general_bp)


    logger.debug("Application running...")

    return app