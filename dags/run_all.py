from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime

with DAG(
    dag_id='run_all_dags_dag',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    default_args = {
        'owner': 'airflow',
    },
    description='A DAG to trigger all other DAGs sequentially',
) as dag:

    trigger_dag1 = TriggerDagRunOperator(
        task_id='trigger_dag1',
        trigger_dag_id='fetch_data_dag',
    )

    trigger_dag2 = TriggerDagRunOperator(
        task_id='trigger_dag2',
        trigger_dag_id='process_data_dag',
    )

    trigger_dag3 = TriggerDagRunOperator(
        task_id='trigger_dag3',
        trigger_dag_id='data_processing_dag',
    )

    trigger_dag4 = TriggerDagRunOperator(
        task_id='trigger_dag4',
        trigger_dag_id='build_and_train_ml_model',
    )

    trigger_dag1 >> trigger_dag2 >> trigger_dag3 >> trigger_dag4