#!/bin/bash

# Wait for PostgreSQL to be ready using Python
echo "Waiting for PostgreSQL to be ready..."
python3 << EOF
import psycopg2
import time
import sys

while True:
    try:
        conn = psycopg2.connect(
            host="postgres",
            port=5432,
            user="kpi_user",
            password="kpi_password",
            database="kpi_db"
        )
        conn.close()
        print("PostgreSQL is ready!")
        break
    except psycopg2.OperationalError:
        print("Waiting for PostgreSQL...")
        time.sleep(1)
EOF

# Initialize Airflow database
echo "Initializing Airflow database..."
airflow db init

# Create admin user
echo "Creating admin user..."
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password admin

echo "Airflow initialization completed!" 