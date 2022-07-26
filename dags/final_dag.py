# Step 1: Importing modules
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
import pandas as pd

# Step 2: Create python function
def read_data():
    sql_stmt = "SELECT * FROM transactions"
    pg_hook = PostgresHook(
        postgres_conn_id='postgres_terminal'
        # schema='db_test'
    )
    pg_conn = pg_hook.get_conn()
    cursor = pg_conn.cursor()
    cursor.execute(sql_stmt)
    return cursor.fetchall()

def process_terminal_data(ti):
    terminal_db = ti.xcom_pull(task_ids=['get_terminal_data'])
    if not terminal_db:
        raise Exception('No data.')

    terminal_db = pd.DataFrame(
        data=terminal_db[0],
        columns=['user_id', 'ts', 'transaction_amount']
    )

    processed_data  = terminal_db.head(2)
    return processed_data

def save_data_to_final_db(processed_data):
    dest = PostgresHook(postgres_conn_id='postgres_results')
    dest_conn = dest.get_conn()
    dest_cursor = dest_conn.cursor()
    data = processed_data.xcom_pull(task_ids=['process_data'])



# Step 3: Default Arguments
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2022, 6, 1),
    "email": ["caroline.kosalka@gmail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

# Step 4: Instantiate a DAG
with DAG(dag_id="final_dag_test", default_args=default_args, schedule_interval=timedelta(1)) as final_dag:

# Step 5:  Set the Tasks
    # first task: load Data From  (hint: Install the psycopg2 module)
    task_read_data = PythonOperator(
        task_id='get_terminal_data',
        python_callable=read_data,
        do_xcom_push=True,
        dag=final_dag

    )

    # second task: Validation task (hint: duplicates) --> leave it for now
    task_process_data = PythonOperator(
        task_id='process_data',
        python_callable=process_terminal_data,
        dag=final_dag
    )

    # third task: Remove passwords & Join tables
    #t3 = PythonOperator(task_id='t3', python_callable=f3, dag=final_dag)

    # fifth task: load the result table to results db
    #t5 = PythonOperator(task_id='t4', python_callable=f3, dag=final_dag)


# Step 6 :  Setting up the Dependecies
#  print_bye_t2.set_upstream(print_hello_t1)
# task_read_data>>task_process_data
#t2>>t3
#t3>>t4