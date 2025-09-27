from sqlalchemy import create_engine
import pandas as pd

# -----------------------------
# Параметры подключения
# -----------------------------
db_user = "postgres"
db_password = "5752063"     # поставь свой пароль
db_host = "localhost"
db_port = "5433"                # проверь в postgresql.conf
db_name = "HospitalManagementSystem"

# Создаем движок подключения
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# -----------------------------
# Проверка соединения
# -----------------------------
try:
    with engine.connect() as conn:
        print("Подключение успешно!")
except Exception as e:
    print("Ошибка подключения:", e)
    exit()


# -----------------------------
tables = ["Patients", "Doctor", "Appointment", "Room", "Ward", "Nurse"]

for table in tables:
    try:
        query = f"SELECT * FROM {table} LIMIT 5;"
        df = pd.read_sql(query, engine)
        print(f"\nТаблица: {table}")
        print(df)
    except Exception as e:
        print(f"Ошибка при выборке из {table}: {e}")
