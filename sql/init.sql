-- Step 2: Basic checks and queries
-- 2.1 View first rows (пример, адаптируй под свои таблицы)
SELECT * FROM patients
LIMIT 10;

-- 2.2 Filter data (пример фильтрации по условию)
SELECT * FROM patients
WHERE gender = 'Female'
LIMIT 10;

-- 2.3 Aggregations and grouping (пример подсчета по отделам)
SELECT dept_id, COUNT(*) AS num_doctors
FROM doctor
GROUP BY dept_id
ORDER BY num_doctors DESC;

-- 2.4 Statistical functions (пример среднего возраста)
SELECT AVG(EXTRACT(YEAR FROM AGE(date_of_birth))) AS avg_age
FROM patients;

-- 2.5 JOIN between tables (пример соединения докторов и записей)
SELECT d.doct_id, d.fname, d.lname, COUNT(a.appointment_id) AS num_appointments
FROM doctor d
LEFT JOIN appointment a ON d.doct_id = a.doct_id
GROUP BY d.doct_id, d.fname, d.lname
ORDER BY num_appointments DESC;

-- Step 3: Analytics topics

-- 3.1 Number of patients by gender
SELECT gender, COUNT(*) AS num_patients
FROM patients
GROUP BY gender
ORDER BY num_patients DESC;

-- 3.2 Average age of patients
SELECT AVG(EXTRACT(YEAR FROM AGE(date_of_birth))) AS avg_age
FROM patients;

-- 3.3 Number of doctors per department
SELECT dept_id, COUNT(*) AS num_doctors
FROM doctor
GROUP BY dept_id
ORDER BY num_doctors DESC;

-- 3.4 Number of appointments per doctor
SELECT d.doct_id, d.fname, d.lname, COUNT(a.appointment_id) AS num_appointments
FROM doctor d
LEFT JOIN appointment a ON d.doct_id = a.doct_id
GROUP BY d.doct_id, d.fname, d.lname
ORDER BY num_appointments DESC;

-- 3.5 Average hospitalization cost per department
SELECT w.dept_id, AVG(b.amount) AS avg_amount
FROM bedrecords b
JOIN bed bd ON b.bed_no = bd.bed_no
JOIN ward w ON bd.ward_no = w.ward_no
GROUP BY w.dept_id
ORDER BY avg_amount DESC;

-- 3.6 Minimum and maximum procedure cost
SELECT MIN(amount) AS min_amount, MAX(amount) AS max_amount
FROM (
    SELECT amount FROM bedrecords
    UNION ALL
    SELECT amount FROM roomrecords
) AS all_amounts;

-- 3.7 Number of patients per year
SELECT EXTRACT(YEAR FROM admission_date) AS year, COUNT(DISTINCT patient_id) AS num_patients
FROM bedrecords
GROUP BY year
ORDER BY year;

-- 3.8 Average number of days patients stay in a ward
SELECT AVG(discharge_date - admission_date) AS avg_days
FROM bedrecords
WHERE discharge_date IS NOT NULL;

-- 3.9 Number of surgeries by type
SELECT surgery_type, COUNT(*) AS num_surgeries
FROM surgeryrecord
GROUP BY surgery_type
ORDER BY num_surgeries DESC;

-- 3.10 Number of nurses and helpers per department
SELECT dept_id,
       SUM(CASE WHEN role = 'nurse' THEN 1 ELSE 0 END) AS num_nurses,
       SUM(CASE WHEN role = 'helper' THEN 1 ELSE 0 END) AS num_helpers
FROM (
    SELECT dept_id, 'nurse' AS role FROM nurse
    UNION ALL
    SELECT dept_id, 'helper' AS role FROM helpers
) AS staff
GROUP BY dept_id
ORDER BY dept_id;
