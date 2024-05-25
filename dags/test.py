from datetime import timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'test_airflow',
    default_args=default_args,
    description='A simple DAG to test Airflow',
    schedule_interval='@once',
)

# Define the Python function to be executed as a task
def print_hello():
    print('Hello, Airflow!')

# Define the task using the PythonOperator
task_hello = PythonOperator(
    task_id='task_hello',
    python_callable=print_hello,
    dag=dag,
)

# Define the task dependencies
task_hello
