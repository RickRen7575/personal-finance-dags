from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

args = {
    'owner': 'renner@amendllc.com',
    'start_date': datetime(2022, 3, 24, 0, 0),
    'random_logic': False
}

dag = DAG(
    'sample_dag',
    schedule_interval="@once",
    default_args=args
)

t1 = DummyOperator(
    task_id='extract_data',
    dag=dag
)

t2 = DummyOperator(
    task_id='load_data',
    dag=dag
)

t3 = DummyOperator(
    task_id='random_task',
    dag=dag
)

t1.set_downstream(t2)
t2.set_downstream(t3)