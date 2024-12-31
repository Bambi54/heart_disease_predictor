import pickle
import pandas as pd
from sklearn.metrics import accuracy_score
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.utils.email import send_email



def monitor_model(params: dict):
    data = pd.read_csv(params['relearn_data'])
    
    X_test = data.drop(columns=['Target'])
    y_test = data['Target']

    with open(params['model'], 'rb') as model_file:
        model = pickle.load(model_file)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    if accuracy < 0.8:
        subject = "Warning: student_dropouts model accuracy dropped below threshold"
        body = f'''The model's accuracy dropped to {accuracy:.2f}
        Please investigate and retrain the model if necessary.'''
        
        recipients = ["aleksander.babij@gmail.com"]
        send_email(to=recipients, subject=subject, html_content=body)
        


with DAG(
    '5_monitoring',
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
    params={
        'relearn_data': 'relearn_data_clean.csv',
        'model': 'model.pkl'
    }
) as dag:

    monitor_model_task = PythonOperator(
        task_id='monitor_model',
        python_callable=monitor_model,
    )

    monitor_model_task