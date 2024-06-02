# Exercises for Basic Operators and Sensors

Create an Airflow DAG with the following tasks for processing files in csv_data folder:

1. List Files in ([csv_data](csv_data)) directory
2. Process the CSV files in ([csv_data](csv_data)) directory by converting each CSV file to Parquet format and saving the new Parquet file in the same directory (or in a new directory).
3. Wait until all Parquet files are present in the destination directory (*hint: use FileSensor*)
4. Indicate completion once all Parquet files are present in the destination directory by printing a successful message. 

Optional:
1. Use ([Jinja templating](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/operators.html#jinja-templating)) to dynamically calculate and display the date three days before the execution date of the current DAG run.
