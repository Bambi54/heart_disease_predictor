from ucimlrepo import fetch_ucirepo
import pandas as pd
from sklearn.model_selection import train_test_split
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os


def fetch_dataset():
    uciml_data = fetch_ucirepo(id=697)
    data = pd.concat([uciml_data.data.features, uciml_data.data.targets], axis=1)
    data.to_csv('data.csv', index=False)


def split_data():
    data = pd.read_csv('data.csv')
    train, test = train_test_split(data, test_size=0.3, random_state=42)
    train.to_csv('train_data.csv', index=False)
    test.to_csv('test_data.csv', index=False)
    os.remove('data.csv')


with DAG(
    dag_id='fetch_data_dag',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    default_args = {
        'owner': 'airflow',
    }
) as dag:
    
    fetch_task = PythonOperator(
        task_id='fetch_dataset',
        python_callable=fetch_dataset,
    )

    split_data_task = PythonOperator(
        task_id='split_data',
        python_callable=split_data,
    )

    fetch_task >> split_data_task