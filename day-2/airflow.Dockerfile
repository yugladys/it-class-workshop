FROM apache/airflow:2.8.3-python3.10

COPY dags/sample*.py /opt/airflow/dags/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

