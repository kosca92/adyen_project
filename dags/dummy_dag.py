from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime
with DAG('example_dag', start_date=datetime(2022, 1, 1)) as dag:
    populate_db = PostgresOperator


    op = DummyOperator(task_id='op')