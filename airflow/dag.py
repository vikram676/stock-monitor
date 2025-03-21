from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'stock_market_pipeline.settings'
import django
django.setup()

from spark_pipeline.data_processing import fetch_and_process_stock_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 3, 20),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'stock_data_pipeline',
    default_args=default_args,
    schedule_interval='@hourly',
) as dag:
    task = PythonOperator(
        task_id='fetch_stock_data',
        python_callable=fetch_and_process_stock_data
    )
