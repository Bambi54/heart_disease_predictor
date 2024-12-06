import pickle
import pandas as pd
from sklearn.metrics import accuracy_score
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator
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
        body = (
            f"The model's accuracy dropped to {accuracy:.2f}, "
            "Please investigate and retrain the model if necessary."
        )
        
        recipients = "aleksander.babij@gmail.com"
        send_email(to=recipients, subject=subject, html_content=body)


with DAG(
    'monitor_model',
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
    params={
        'relearn_data': 'relearn_data_clean.csv',
        'model': 'model.pkl'
    }
) as dag:
    
    email_test_task = EmailOperator(
        task_id='send_test_email',
        to='aleksander.babij@gmail.com',
        subject='Test Email from Airflow using AWS SES',
        html_content='This is a test email sent using AWS SES SMTP configuration.',
    )

    # monitor_model_task = PythonOperator(
    #     task_id='monitor_model',
    #     python_callable=monitor_model,
    # )

    email_test_task