import os

BASE_DIR = os.path.dirname(__file__)

MODEL_PATH = os.path.join(BASE_DIR, "models_store", "iris_model.pkl")

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "3306",
    "database": "iris_db",
    "charset": "utf8mb4"
}