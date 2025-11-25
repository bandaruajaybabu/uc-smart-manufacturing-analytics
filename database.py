import psycopg2
import os
import csv

# -----------------------------
# PostgreSQL connection details
# -----------------------------
DB_NAME = "uc_smart_mfg"
DB_USER = "postgres"       # your postgres username
DB_PASSWORD = "Y2ru189@704"  # replace with your postgres password
DB_HOST = "localhost"
DB_PORT = "5432"

# -----------------------------
# Connect to PostgreSQL
# -----------------------------
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        print("Connected to PostgreSQL database!")
        return conn
    except Exception as e:
        print("Error connecting to database:", e)
        return None

# -----------------------------
# Load CSV into a table safely
# -----------------------------
def load_csv(conn, table_name, csv_path):
    if not os.path.exists(csv_path):
        print(f"CSV file not found: {csv_path}")
        return

    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
    count = cursor.fetchone()[0]
    if count > 0:
        print(f"Table '{table_name}' already has data. Skipping CSV load.")
        cursor.close()
        return

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)  # skip header
        for row in reader:
            placeholders = ','.join(['%s'] * len(row))
            query = f"INSERT INTO {table_name} ({','.join(headers)}) VALUES ({placeholders})"
            try:
                cursor.execute(query, row)
            except Exception as e:
                print(f"Error inserting row {row}: {e}")
    conn.commit()
    cursor.close()
    print(f"CSV loaded into {table_name} successfully!")
