from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from extract_data import extract_transform_data
from train_model import train_model, evaluate_model
from predict_model import predict_model

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'ecommerce_pipeline',
    default_args=default_args,
    description='Pipeline para treinamento e previsão de modelo de e-commerce',
    schedule_interval=None,
)

# Etapa 1: Extração e transformação dos dados
def extract_transform():
    data = extract_transform_data('C:\Users\allis\Downloads\MDCC\Untitled Folder\dados.csv')

# Etapa 2: Treinamento do modelo
def train():
    model = train_model('/path/to/training_data.csv')

# Etapa 3: Avaliação do modelo
def evaluate():
    accuracy = evaluate_model(model, '/path/to/test_data.csv')

# Etapa 4: Previsão do modelo
def predict():
    predictions = predict_model(model, '/path/to/new_data.csv')

# Definir tarefas
extract_transform_task = PythonOperator(
    task_id='extract_transform_task',
    python_callable=extract_transform,
    dag=dag,
)

train_task = PythonOperator(
    task_id='train_task',
    python_callable=train,
    dag=dag,
)

evaluate_task = PythonOperator(
    task_id='evaluate_task',
    python_callable=evaluate,
    dag=dag,
)

predict_task = PythonOperator(
    task_id='predict_task',
    python_callable=predict,
    dag=dag,
)

# Definir dependências entre tarefas
extract_transform_task >> train_task >> evaluate_task >> predict_task
