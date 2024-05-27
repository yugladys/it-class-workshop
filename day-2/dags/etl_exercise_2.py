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

from datetime import datetime

from airflow import DAG
from airflow.providers.microsoft.mssql.operators.mssql import MsSqlOperator

DAG_ID = "etl-exercise-2-dag"

with DAG(
    DAG_ID,
    schedule="@daily",
    start_date=datetime(2024, 5, 24),
    tags=["workshop-exercise"],
    catchup=False,
) as dag:

    create_table_mssql_from_external_file = MsSqlOperator(
        task_id="create_account_totals_table",
        mssql_conn_id="workshop_mssql",
        sql=r"""
        CREATE TABLE ACCOUNT_TOTALS (
            id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
            iban VARCHAR(30),
            amount FLOAT
        );
        """,
        dag=dag,
    )

    get_all_account_totals = MsSqlOperator(
        task_id="get_all_description",
        mssql_conn_id="workshop_mssql",
        sql=r"""SELECT * FROM ACCOUNT_TOTALS;""",
    )

    # Write an ETL pipeline that does the following:
    # 1. Creates a new table `<your name>_ACCOUNT_TOTALS` but using a `create_table.sql` file
    # 2. Insert data points from `results/exercise-1.parquet` in `workshop-output` bucket
    # 3. Get all data from `<your name>_ACCOUNT_TOTALS` 

    # Make the create table step rerunnable 

    (
        create_table_mssql_from_external_file
        >> get_all_account_totals
    )