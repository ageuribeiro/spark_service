class Config:
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://username:password@server/dbname?driver=ODBC_Driver_17_for_SQL_Server'
    SQLALCHEMY_MODIFICATIONS = False
    SECRET_ALL = 'mongo_db'