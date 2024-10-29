from params_config import Config
from connection import MySQLConnection

config = Config()
host, port, user, password, database = config.getDBConfig()

connection = MySQLConnection(host, port, user, password, database)
connection.connect()
cursor = connection.createCursor()
