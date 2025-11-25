# database.py
import pandas as pd
import os

def load_csv(table_name):
    """
    Load CSV for the given table name
    """
    project_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(project_dir, "data", f"{table_name}.csv")
    
    if not os.path.exists(csv_path):
        print(f"CSV file not found: {csv_path}")
        return None
    
    df = pd.read_csv(csv_path)
    print(f"{table_name}.csv loaded, {len(df)} rows")
    return df

if __name__ == "__main__":
    for table in ["students", "courses", "enrollments"]:
        load_csv(table)
