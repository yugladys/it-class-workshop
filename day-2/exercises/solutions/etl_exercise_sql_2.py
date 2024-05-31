# Code template from: https://airflow.apache.org/docs/apache-airflow-providers-microsoft-mssql/stable/_modules/tests/system/providers/microsoft/mssql/example_mssql.html
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""
Example use of MsSql related operators.
"""
from __future__ import annotations
import pandas as pd

from datetime import datetime

from airflow import DAG
from airflow.providers.microsoft.mssql.operators.mssql import MsSqlOperator
from airflow.providers.amazon.aws.transfers.s3_to_sql import S3ToSqlOperator


DAG_ID = "etl-exercise-sql-2-dag"

S3_CONN_ID = "workshop_s3"
SRC_BUCKET_NAME = "workshop-output"
SRC_FILE = "gladys.parquet"

SQL_CONN_ID = "workshop_mssql"
COLUMNS = ["iban", "amount"]
DB_TABLE = "ACCOUNT_TOTALS"


with DAG(
    DAG_ID,
    schedule_interval=None,
    start_date=datetime(2024, 5, 24),
    tags=["workshop-exercise"],
    catchup=False,
) as dag:

    create_table_mssql_from_external_file = MsSqlOperator(
        task_id="create_account_totals_table",
        mssql_conn_id=SQL_CONN_ID,
        sql="/create_table.sql",
        dag=dag,
    )

    def parse_parquet_to_list(filepath):
        df = pd.read_parquet(filepath)
        values_list = df.reset_index()[COLUMNS].values.tolist()
        return values_list
    

    transfer_s3_to_sql = S3ToSqlOperator(
        aws_conn_id=S3_CONN_ID,
        task_id="transfer_s3_to_sql",
        s3_bucket=SRC_BUCKET_NAME,
        s3_key=f"results/{SRC_FILE}",
        table=DB_TABLE,
        column_list=COLUMNS,
        parser=parse_parquet_to_list,
        sql_conn_id=SQL_CONN_ID,
    )

    get_all_account_totals = MsSqlOperator(
        task_id="get_all_description",
        mssql_conn_id=SQL_CONN_ID,
        sql=f"SELECT * FROM {DB_TABLE};",
    )

    # Write an ETL pipeline that does the following:
    # 1. Creates a new table `<your name>_ACCOUNT_TOTALS` but using a `create_table.sql` file
    # 2. Downloads file `results/<yourname>.parquet` from `workshop-output` bucket to local directory
    # 3. Insert rows from parquet file to database table
    # 4. Select all data from `<your name>_ACCOUNT_TOTALS` table

    # Make the create table step rerunnable 

    # Hints: you can use S3ToSqlOperator, and some functions in MsSqlHook, S3Hook

    (
        create_table_mssql_from_external_file
        >> transfer_s3_to_sql
        >> get_all_account_totals
    )