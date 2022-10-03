from airflow import DAG
from airflow.operators.python import PythonOperator

import os
import time
import requests
from datetime import datetime


def run_job1():
    BASE_DIR = os.environ.get("BASE_DIR")

    if not BASE_DIR:
        print("BASE_DIR environment variable must be set")
        exit(1)

    JOB1_PORT = 8081

    RAW_DIR = os.path.join(BASE_DIR, "raw", "sales", "2022-08-09")

    print("Starting job1:")
    resp = requests.post(
        url=f'http://localhost:{JOB1_PORT}/',
        json={
            "date": "2022-08-09",
            "raw_dir": RAW_DIR
        }
    )
    assert resp.status_code == 201
    print("job1 completed!")


def run_job2():
    BASE_DIR = os.environ.get("BASE_DIR")

    if not BASE_DIR:
        print("BASE_DIR environment variable must be set")
        exit(1)

    JOB2_PORT = 8082

    RAW_DIR = os.path.join(BASE_DIR, "raw", "sales", "2022-08-09")
    STG_DIR = os.path.join(BASE_DIR, "stg", "sales", "2022-08-09")

    print("Starting job2:")
    resp = requests.post(
        url=f'http://localhost:{JOB2_PORT}/',
        json={
            "raw_dir": RAW_DIR,
            "stg_dir": STG_DIR
        }
    )
    assert resp.status_code == 201
    print("job2 completed!")


'''if __name__ == '__main__':
    run_job1()
    time.sleep(3)
    run_job2()
'''


def ooo():
    print(1)


dag = DAG(
    dag_id='process_sales',
    start_date=datetime(2022, 9, 15),
    end_date=datetime(2022, 9, 16),
    schedule_interval="* * * * *"
)

extract_data_from_api = PythonOperator(
    task_id="extract_data_from_api",
    python_callable=run_job1,
    dag=dag
)


convert_to_avro = PythonOperator(
    task_id="convert_to_avro",
    python_callable=ooo,
    dag=dag
)


extract_data_from_api >> convert_to_avro
