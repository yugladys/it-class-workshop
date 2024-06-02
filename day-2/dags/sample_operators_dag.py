from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.decorators import task

from datetime import datetime, timedelta
import pandas as pd


default_args = {
        "owner": "airflow",
        "depends_on_past": False,
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    }

def read_csv(file_path: str):
    df = pd.read_csv(file_path)
    print(df.head())

@task
def final_python_function():
    print("The final task of the DAG ran successfully")


with DAG('operators-sample-dag',
        default_args = default_args,
        start_date = datetime(2024,6,1),
        schedule_interval = "30 9 * * *", #09:30 every day
        # catchup = False,
        tags = ["workshop"],
        ) as dag:


    start_task = BashOperator(
        task_id='start_dag',
        bash_command='echo "DAG successfully started!"',
    )

    read_data_task = PythonOperator(
        task_id='read_data_from_csv',
        python_callable=read_csv,
        op_args=['day-2/s3_data/workshop/input.csv']
    )

    final_task = final_python_function()

    start_task >> read_data_task >> final_task