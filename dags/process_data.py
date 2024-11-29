from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd


def clean_data():
    datasets = ['model_data.csv', 'relearn_data.csv']

    for dataset in datasets:
        data = pd.read_csv(dataset)
        data.drop_duplicates(inplace=True)

        numeric_columns = data.select_dtypes(include=['number']).columns
        data[numeric_columns].fillna(data[numeric_columns].mean(), inplace=True)

        data.to_csv(dataset, index=False)


def preprocess_data():
    datasets = ['model_data', 'relearn_data']

    for dataset in datasets:
        uncleaned_dataset = f'{dataset}.csv'
        clean_dataset = f'{dataset}_clean.csv'

        data = pd.read_csv(uncleaned_dataset)
        normalized_data = MinMaxScaler().fit_transform(data.select_dtypes(include=['float', 'int']))

        data.update(pd.DataFrame(normalized_data, columns=data.select_dtypes(include=['float', 'int']).columns))
        data.to_csv(clean_dataset, index=False)


with DAG(
    dag_id='process_data_dag',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    default_args = {
        'owner': 'airflow',
    }
) as dag:
    
    clean_data_task = PythonOperator(
        task_id='clean_data',
        python_callable=clean_data,
    )

    preprocess_data_task = PythonOperator(
        task_id='preprocess_data',
        python_callable=preprocess_data,
    )

    clean_data_task >> preprocess_data_task
