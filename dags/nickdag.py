"""
Code that goes along with the Airflow located at:
http://airflow.readthedocs.org/en/latest/tutorial.html
"""

# Step 1: Importing modules

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator

# Step 2: Create python function
def print_hello():
    return 'welcome'

def print_goodbye():
    return 'goodbye'


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
with DAG(dag_id="tutorial", default_args=default_args, schedule_interval=timedelta(1)) as first_dag:

    # Step 5:  Set the Tasks
    print_hello_t1 = PythonOperator(task_id='t1', python_callable=print_hello, dag= first_dag)
    print_bye_t2 = PythonOperator(task_id='t2', python_callable=print_goodbye, dag=first_dag)


# Step 6 :  Setting up the Dependecies
#  print_bye_t2.set_upstream(print_hello_t1)
print_hello_t1>>print_bye_t2

