# Exercises for S3 and MS SQL Operators

This requires you to build simple pipelines that does basic data transformation and use the S3 and MS SQL Operators.

1. Create a docker compose file ([compose.yaml](../compose.yaml)) that runs a local S3 and MSSQL
2. Create a DAG that uses S3 operators ([etl_exercise_s3.py](../dags/etl_exercise_s3.py))
3. Create a DAG that uses MSSQL operators ([etl_exercise_sql.py](../dags/etl_exercise_sql.py))
4. Test and run your DAGs by rebuilding image in [airflow.Dockerfile](../airflow.Dockerfile)
5. Scale down ONLY the scheduler & webserver deployments, and worker statefulset to 0 then back to 1 replica. This will restart the pods with the updated image containing the DAG changes.
