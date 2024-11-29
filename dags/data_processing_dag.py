import pandas as pd
from sklearn.model_selection import train_test_split
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def split_data(params:dict):
    data = pd.read_csv(params['model_data'])
    
    train, test = train_test_split(data, test_size=0.3, random_state=42)
    train.to_csv(params['train_data'], index=False)
    test.to_csv(params['test_data'], index=False)
    

with DAG(
    'data_processing_dag',
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
    params={
        'model_data': 'model_data_clean.csv',
        'train_data': 'train_data_clean.csv',
        'test_data': 'test_data_clean.csv',
        'model': 'model.pkl'
    }
) as dag:
    
    task = PythonOperator(
        task_id='split_data',
        python_callable=split_data
    )

    task
