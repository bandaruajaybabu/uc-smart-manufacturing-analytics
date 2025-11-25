from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
sys.path.insert(0, '/path/to/etl')
from etl_pipeline import etl_pipeline

with DAG('uc_capstone', start_date=datetime(2025, 11, 24), schedule_interval='@daily', catchup=False) as dag:
    run_etl = PythonOperator(task_id='run_etl', python_callable=etl_pipeline)