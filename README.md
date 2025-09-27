# Hospital Analytics Project

## Company
**MediData Analytics** – a data analytics company specializing in healthcare analytics, helping hospitals and clinics to monitor patients, staff, and resources efficiently.

## Project Overview
This project is focused on analyzing hospital management data. Using a sample hospital dataset, we perform SQL queries and Python-based analysis to extract insights such as patient demographics, doctor assignments, appointment statistics, bed utilization, and surgery records. The project aims to demonstrate how structured data can be used for operational and strategic decision-making in a hospital environment.

## Screenshot
![Hospital Analytics Dashboard](erd/hospital_erd.png)
*Screenshot of the database ERD – main analytics view (placeholder, can be updated later).*

## Project Structure
```
hospital-analytics/
│── sql/
│ ├── Hospital_Management_System.sql # SQL script to create and populate the database
│ └── init.sql # optional initialization script
│
│── data/
│ ├── patients.xlsx # sample dataset in Excel
│ └── patients.csv # sample dataset in CSV
│
│── erd/
│ └── hospital_erd.png # ERD diagram of the database
│
│── main.py # Python script with SQL queries
│── requirements.txt # Python dependencies
│── README.md # this file
```

## Setup Instructions
1. **Install PostgreSQL** and create a database:
```bash
create database HospitalManagementSystem
psql -U postgres -d HospitalManagementSystem -f sql/Hospital_Management_System.sql
pip install -r requirements.txt
python main.py
```

## Analytics

Here are some queries we analyze in this project:
1. Number of patients by gender.
2. Average patient age.
3. Number of doctors per department.
4. Number of appointments per doctor.
5. Average hospital stay duration by department.
6. Minimum and maximum procedure costs.
7. Number of patients admitted per year.
8. Average number of days per bed usage.
9. Number of surgeries by type.
10. Staff count per department.


## Tools and Resources

1. PostgreSQL for database management
2. Python for scripting and analysis
3. Libraries: psycopg2, pandas, openpyxl
4. Apache Superset (optional, for visualization)


