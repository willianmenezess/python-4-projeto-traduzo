from pymongo import MongoClient
from os import environ

# Conecta no Mongo, pela variável ambiente definida no Docker Compose
client = MongoClient(environ.get("MONGO_URI"))

# Cria um banco de dados chamado test_db_traduzo
db = client["test_db_traduzo"]
