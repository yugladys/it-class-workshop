# Code template from: https://airflow.apache.org/docs/apache-airflow-providers-amazon/2.2.0/operators/s3.html

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

from airflow.models.dag import DAG
# from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.amazon.aws.operators.s3 import S3CreateBucketOperator
# from airflow.providers.amazon.aws.transfers.local_to_s3 import LocalFilesystemToS3Operator
from airflow.utils.dates import days_ago

S3_CONN_ID = "workshop_s3"
SRC_BUCKET_NAME = "workshop"
SRC_FILE = "input.csv"
DEST_BUCKET_NAME = "workshop-output"
DEST_FILE = "yourname.parquet"

with DAG(
    dag_id="etl-exercise-s3-dag",
    schedule_interval=None,
    start_date=days_ago(2),
    max_active_runs=1,
    tags=["workshop-exercise"],
) as dag:


    create_bucket = S3CreateBucketOperator(
        task_id="s3_bucket_dag_create",
        aws_conn_id=S3_CONN_ID,
        bucket_name=DEST_BUCKET_NAME,
    )

    # Write an ETL pipeline that does the following:
    # 1. Downloads file `SRC_FILE` from `workshop` bucket to local directory
    # 2. Computes the sum of amounts per iban from given data (you may use pandas)
    # 3. Saves the resulting dataframe as `<yourname>.parquet` file
    # 4. Uploads the resulting parquet file to `workshop-output` bucket under `results/<yourname>.parquet`

    # `workshop` bucket is already created and contains files when you start the s3proxy container

    # Hints: you can use LocalFilesystemToS3Operator, and/or some functions in S3Hook

    create_bucket