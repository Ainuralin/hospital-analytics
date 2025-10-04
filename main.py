from sqlalchemy import create_engine
import pandas as pd

# Параметры подключения
db_user = "postgres"
db_password = "5752063"
db_host = "localhost"
db_port = "5433"
db_name = "HospitalManagementSystem"

# Подключение
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# Проверка соединения
try:
    with engine.connect() as conn:
        print("Подключение успешно!")
except Exception as e:
    print("Ошибка подключения:", e)
    exit()

print("1. Количество пациентов по полу")

query1 = """
SELECT gender AS "Пол пациента", COUNT(*) AS "Количество пациентов"
FROM patients
GROUP BY gender
ORDER BY "Количество пациентов" DESC;
"""
patients_by_gender = pd.read_sql(query1, engine)
print(patients_by_gender)


print("\n2. Средний возраст пациентов")

query2 = """
SELECT AVG(EXTRACT(YEAR FROM AGE(date_of_birth))) AS "Средний возраст"
FROM patients;
"""
avg_age = pd.read_sql(query2, engine)
print(avg_age)


print("\n3. Количество врачей по отделениям (с названиями отделений)")

query3 = """
SELECT d.dept_id AS "ID отделения", dept.dept_name AS "Название отделения", COUNT(*) AS "Количество врачей"
FROM doctor d
JOIN department dept ON d.dept_id = dept.dept_id
GROUP BY d.dept_id, dept.dept_name
ORDER BY "Количество врачей" DESC;
"""
doctors_per_dept = pd.read_sql(query3, engine)
print(doctors_per_dept)


print("\n4. Количество приёмов у каждого врача")

query4 = """
SELECT d.doct_id AS "ID врача",
        d.fname || ' ' || d.lname AS "ФИО врача",
        COUNT(a.appointment_id) AS "Количество приёмов"
FROM doctor d
LEFT JOIN appointment a ON d.doct_id = a.doct_id
GROUP BY d.doct_id, d.fname, d.lname
ORDER BY "Количество приёмов" DESC;
"""
appointments_per_doctor = pd.read_sql(query4, engine)
print(appointments_per_doctor)


print("\n5. Средняя стоимость госпитализации по отделениям")

query5 = """
SELECT w.dept_id AS "ID отделения", dept.dept_name AS "Название отделения", AVG(b.amount) AS "Средняя стоимость госпитализации"
FROM bedrecords b
JOIN bed bd ON b.bed_no = bd.bed_no
JOIN ward w ON bd.ward_no = w.ward_no
JOIN department dept ON w.dept_id = dept.dept_id
GROUP BY w.dept_id, dept.dept_name
ORDER BY "Средняя стоимость госпитализации" DESC;
"""
avg_cost_per_dept = pd.read_sql(query5, engine)
print(avg_cost_per_dept)


print("\n6. Минимальная и максимальная стоимость процедур")

query6 = """
SELECT MIN(amount) AS "Минимальная стоимость процедуры",
        MAX(amount) AS "Максимальная стоимость процедуры"
FROM (
    SELECT amount FROM bedrecords
    UNION ALL
    SELECT amount FROM roomrecords
) AS all_costs;
"""
min_max_cost = pd.read_sql(query6, engine)
print(min_max_cost)


print("\n7. Количество пациентов по годам")

query7 = """
SELECT EXTRACT(YEAR FROM admission_date) AS "Год", COUNT(DISTINCT patient_id) AS "Количество пациентов"
FROM bedrecords
GROUP BY "Год"
ORDER BY "Год";
"""
patients_per_year = pd.read_sql(query7, engine)
print(patients_per_year)


print("\n8. Среднее количество дней пребывания пациентов в отделении")

query8 = """
SELECT AVG(discharge_date - admission_date) AS "Среднее количество дней пребывания"
FROM bedrecords
WHERE discharge_date IS NOT NULL;
"""
avg_stay = pd.read_sql(query8, engine)
print(avg_stay)


print("\n9. Количество операций по типам")

query9 = """
SELECT surgery_type AS "Тип операции", COUNT(*) AS "Количество операций"
FROM surgeryrecord
GROUP BY surgery_type
ORDER BY "Количество операций" DESC;
"""
surgeries_by_type = pd.read_sql(query9, engine)
print(surgeries_by_type)


print("\n10. Количество медсестёр и помощников по отделениям (с названиями отделений)")

query10 = """
SELECT dept.dept_id AS "ID отделения", dept.dept_name AS "Название отделения",
       SUM(CASE WHEN role = 'nurse' THEN 1 ELSE 0 END) AS "Количество медсестёр",
       SUM(CASE WHEN role = 'helper' THEN 1 ELSE 0 END) AS "Количество помощников"
FROM (
    SELECT dept_id, 'nurse' AS role FROM nurse
    UNION ALL
    SELECT dept_id, 'helper' AS role FROM helpers
) AS staff
JOIN department dept ON staff.dept_id = dept.dept_id
GROUP BY dept.dept_id, dept.dept_name
ORDER BY "Название отделения";
"""
nurses_helpers_per_dept = pd.read_sql(query10, engine)
<<<<<<< HEAD
print(nurses_helpers_per_dept)
=======
print(nurses_helpers_per_dept)
>>>>>>> 0561f09 (Update project and add .gitignore)
