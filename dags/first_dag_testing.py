from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 24),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG('test_dag', default_args=default_args, schedule_interval=timedelta(days=1)) as dag:
    # Define your tasks here
    start_task = DummyOperator(task_id='start_task')
    end_task = DummyOperator(task_id='end_task')

    start_task >> end_task
