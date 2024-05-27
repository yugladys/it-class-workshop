from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

from datetime import timedelta
from dateutil.relativedelta import relativedelta, TU

def get_second_day_of_week(run_date):
    tuesday_date = (run_date + relativedelta(weekday=TU(-1))).strftime('%Y%m%d')
    return tuesday_date

cfg = { 
    "dag_id": "bash-sample-dates-dag",
    "start_date": days_ago(2),
    "schedule_interval": "30 1 * * *",
    "default_args": {
        "owner": "me",
        "depends_on_past": False,
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=10),
        # "catchup": False,
    },
    "user_defined_macros": {
        "get_second_day_of_week": get_second_day_of_week,
    },
    "tags": ["workshop"],
}

with DAG(
    **cfg
) as dag:

    GET_MONDAY_DATE = "echo Monday: {{ macros.ds_format(macros.ds_add(ds, -macros.datetime.weekday(execution_date)), '%Y-%m-%d', '%Y%m%d') }}"
    GET_TUESDAY_DATE = "echo Tuesday: {{ get_second_day_of_week(execution_date) }}"

    task_1 = BashOperator(
        task_id='bash_monday_macros',
        bash_command=GET_MONDAY_DATE,
    )

    task_2 = BashOperator(
        task_id='bash_tuesday_user_macros',
        bash_command=GET_TUESDAY_DATE,
        # bash_command=GET_MONDAY_DATE,
    )

    task_1 >> task_2
