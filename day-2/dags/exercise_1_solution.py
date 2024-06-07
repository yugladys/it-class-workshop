from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.sensors.filesystem import FileSensor
from airflow.decorators import task

from datetime import datetime, timedelta
import pandas as pd
import os


default_args = {
        "owner": "airflow",
        "depends_on_past": False,
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    }

def convert_csv_to_parquet(source_dir: str, destination_dir: str):
    for filename in os.listdir(source_dir):
        if filename.endswith('.csv'):
            csv_path = os.path.join(source_dir, filename)
            df = pd.read_csv(csv_path)

            parquet_path = os.path.join(destination_dir, filename.replace('.csv', '.parquet'))
            df.to_parquet(parquet_path)
            print(f"Converted {filename} from csv to parquet.")


@task
def final_task():
    print("All Parquet files are present.")


with DAG('process_csv_file',
        default_args = default_args,
        start_date = datetime(2024,6,1),
        schedule_interval = "30 9 * * *", #09:30 every day
        # catchup = False,
        tags = ["workshop-exercise"],
        ) as dag:


    list_files = BashOperator(
        task_id='list_files',
        bash_command='ls -l /Users/us74co/it-class-workshop/day-2/csv_data',
    )

    convert_files = PythonOperator(
        task_id='convert_from_csv_to_parquet',
        python_callable=convert_csv_to_parquet,
        op_args=['/Users/us74co/it-class-workshop/day-2/csv_data', '/Users/us74co/it-class-workshop/day-2/csv_data']
    )

    wait_for_parquet_files = FileSensor(
        task_id='wait_for_parquet_files',
        fs_conn_id='fs_default',
        filepath='/Users/us74co/it-class-workshop/day-2/csv_data/*.parquet',
        poke_interval=30,
        timeout=600,
    )

    successful_dag_run = final_task()

    list_files >> convert_files >> wait_for_parquet_files >> successful_dag_run