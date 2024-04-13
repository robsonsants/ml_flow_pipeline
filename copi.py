from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def extract(**kwargs):
    # código para extração

def transform(**kwargs):
    # código para transformação

def train(**kwargs):
    # código para treinamento

def predict(**kwargs):
    # código para previsão

dag = DAG('my_dag', start_date=datetime(2022, 1, 1))

extract = PythonOperator(task_id='extract', python_callable=extract, provide_context=True, dag=dag)
transform = PythonOperator(task_id='transform', python_callable=transform, provide_context=True, dag=dag)
train = PythonOperator(task_id='train', python_callable=train, provide_context=True, dag=dag)
predict = PythonOperator(task_id='predict', python_callable=predict, provide_context=True, dag=dag)

extract >> transform >> train >> predict
