from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd

def calculate_dau():
    df = pd.read_csv('data/events.csv', parse_dates=['timestamp'])
    df['date'] = df['timestamp'].dt.date
    dau = df.groupby('date')['user_id'].nunique().reset_index()
    dau.to_csv('data/dau.csv', index=False)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dau_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
)

task = PythonOperator(
    task_id='calculate_dau',
    python_callable=calculate_dau,
    dag=dag
)
