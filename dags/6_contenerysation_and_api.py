from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='6_contenerysation_and_api',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    default_args = {
        'owner': 'airflow',
    },
    description='A DAG to trigger all other DAGs sequentially',
) as dag:

    start_docker = BashOperator(
        task_id='start_docker_compose',
        bash_command='docker-compose up'
    )

    stop_docker = BashOperator(
        task_id='stop_docker_compose',
        bash_command='docker-compose down'
    )

    stop_docker >> start_docker