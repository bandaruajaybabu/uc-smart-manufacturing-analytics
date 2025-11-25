from database import connect_db, load_csv
import os

if __name__ == "__main__":
    conn = connect_db()
    if not conn:
        exit(1)

    project_dir = os.path.dirname(os.path.abspath(__file__))

    # Load CSVs safely if tables are empty
    load_csv(conn, "students", os.path.join(project_dir, "data", "students.csv"))
    load_csv(conn, "courses", os.path.join(project_dir, "data", "courses.csv"))
    load_csv(conn, "enrollments", os.path.join(project_dir, "data", "enrollments.csv"))

    # Display tables
    cursor = conn.cursor()
    cursor.execute("SELECT tablename FROM pg_tables WHERE schemaname='public';")
    tables = [t[0] for t in cursor.fetchall()]
    print("Tables in database:", tables)

    # Show first 5 rows from each table
    for table in tables:
        cursor.execute(f"SELECT * FROM {table} LIMIT 5;")
        rows = cursor.fetchall()
        print(f"\nFirst 5 rows from {table}:")
        for row in rows:
            print(row)
    cursor.close()
    conn.close()
