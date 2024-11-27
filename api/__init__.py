from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient

db = SQLAlchemy()
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["logs"]

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://username:password@server/database?driver=ODBC+Driver+17+for+SQL+Server"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from .v1.routes import api_v1
    app.register_blueprint(api_v1, url_prefix="/api/v1")

    return app