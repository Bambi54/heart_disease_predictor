import pickle
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from tpot import TPOTClassifier
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def split_data(params:dict):
    data = pd.read_csv(params['model_data'])
    
    train, test = train_test_split(data, test_size=0.3, random_state=42)
    train.to_csv(params['train_data'], index=False)
    test.to_csv(params['test_data'], index=False)


def train_model(params: dict):
    data = pd.read_csv(params['train_data'])
    X_train = data.drop(columns=['Target'])
    y_train = data['Target']

    tpot = TPOTClassifier(verbosity=2, generations=5, population_size=20, random_state=42)
    tpot.fit(X_train, y_train)
    
    with open(params['model'], 'wb+') as model_file:
        pickle.dump(tpot.fitted_pipeline_, model_file)
        logger.info(f"Model saved to {params['model']}.")
    

def evaluate_model(params: dict):
    logger.info("Starting model evaluation.")
    data = pd.read_csv(params['test_data'])
    logger.info("Test data loaded successfully.")
    
    X_test = data.drop(columns=['Target'])
    y_test = data['Target']

    with open(params['model'], 'rb') as model_file:
        model = pickle.load(model_file)
        logger.info(f"Model loaded from {params['model']}.")

    y_pred = model.predict(X_test)
    logger.info("Predictions generated.")

    accuracy = accuracy_score(y_test, y_pred)
    
    logger.info(f"Accuracy: {accuracy}")
    
    report = f"Accuracy: {accuracy}"
    with open('evaluation_report.txt', 'w+') as report_file:
        report_file.write(report)
        logger.info("Evaluation report written to evaluation_report.txt.")


with DAG(
    '4_building_model',
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
    params={
        'model_data': 'model_data_clean.csv',
        'train_data': 'train_data_clean.csv',
        'test_data': 'test_data_clean.csv',
        'model': '/opt/airflow/shared/model.pkl'
    }
) as dag:

    train_test_split_task = PythonOperator(
        task_id='train_test_split',
        python_callable=split_data,
    )

    train_model_task = PythonOperator(
        task_id='train_model',
        python_callable=train_model,
    )

    evaluate_model_task = PythonOperator(
        task_id='evaluate_model',
        python_callable=evaluate_model,
    )

    train_test_split_task >> train_model_task >> evaluate_model_task
