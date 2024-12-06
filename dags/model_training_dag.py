import pickle
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score
from tpot import TPOTClassifier
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def train_model(params: dict):
    data = pd.read_csv(params['train_data'])
    X_train = data.drop(columns=['Target'])
    y_train = data['Target']

    tpot = TPOTClassifier(verbosity=2, generations=5, population_size=20, random_state=42)
    tpot.fit(X_train, y_train)
    
    pickle.dump(tpot, params['model'])
    

def evaluate_model(params: dict):
    data = pd.read_csv(params['test_data'])
    X_test = data.drop(columns=['Target'])
    y_test = data['Target']
    model = pickle.load(params['model'])

    print('before model prediction')
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    
    report = f"Accuracy: {accuracy}\nPrecision: {precision}\nRecall: {recall}\n"
    
    print('before report write')
    with open('evaluation_report.txt', 'w+') as f:
        f.write(report)


with DAG(
    'build_and_train_ml_model',
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

    train_model_task = PythonOperator(
        task_id='train_model',
        python_callable=train_model,
    )

    evaluate_model_task = PythonOperator(
        task_id='evaluate_model',
        python_callable=evaluate_model,
    )

    train_model_task >> evaluate_model_task
