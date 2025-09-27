# Hospital Analytics Project

## Company
You work as a data analyst at **MediCare Analytics**, a fictional company providing analytics for hospital management and healthcare operations.

## Project Overview
This project demonstrates database analytics for a hospital management system. It uses real-like hospital data to analyze patient admissions, doctor activities, room and bed usage, appointments, surgeries, and staff schedules. The goal is to practice SQL queries, joins, aggregations, and Python-based data analysis.

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
Number of patients by gender.
Average patient age.
Number of doctors per department.
Number of appointments per doctor.
Average hospital stay duration by department.
Minimum and maximum procedure costs.
Number of patients admitted per year.
Average number of days per bed usage.
Number of surgeries by type.
Staff count per department.


## Tools and Resources

PostgreSQL for database management
Python for scripting and analysis
Libraries: psycopg2, pandas, openpyxl
Apache Superset (optional, for visualization)


