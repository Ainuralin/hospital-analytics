# config.py
from sqlalchemy import create_engine

# ===================== ПАРАМЕТРЫ ПОДКЛЮЧЕНИЯ =====================
DB_USER = "postgres"
DB_PASSWORD = "5752063"
DB_HOST = "localhost"
DB_PORT = "5433"
DB_NAME = "HospitalManagementSystem"

# ===================== СОЗДАНИЕ ENGINE =====================
engine = create_engine(
    f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)
