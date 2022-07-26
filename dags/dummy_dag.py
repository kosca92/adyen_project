from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow import DAG
from airflow.hooks.postgres_hook import PostgresHook
dag_params = {
    'dag_id': 'postgres_job',
    'start_date':datetime(2022, 5, 1),
    'schedule_interval': timedelta(seconds=60)
}
with DAG(**dag_params) as dag:
    src = PostgresHook(postgres_conn_id='postgres_terminal')
    dest = PostgresHook(postgres_conn_id='postgres_results')
    src_conn = src.get_conn()
    cursor = src_conn.cursor()
    dest_conn = dest.get_conn()
    dest_cursor = dest_conn.cursor()
    cursor.execute("SELECT * FROM transactions WHERE transaction_amount < 43")
    dest.insert_rows(table="transactions", rows=cursor)







