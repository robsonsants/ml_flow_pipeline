# Etapa 1: Faça as importações
#A primeira etapa é importar as classes de que você precisa. Para criar uma DAG no Airflow, 
#você sempre deve importar a classe DAG. Depois da classe DAG, vêm as importações de Operators. 
#Basicamente, para cada Operator que deseja utilizar, deve-se fazer a importação correspondente. 
#Finalmente, o último import geralmente é a classe de data e hora, pois você precisa especificar uma data de início para o sua DAG.
from datetime import datetime
from random import randint

from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator

#Etapa 2: Criar o objeto DAG do Airflow

def _choosing_best_model(ti):

    accuracies = ti.xcom_pull(task_ids=['training_model_A', 'training_model_B', 'training_model_C'])

    if max(accuracies) > 8:
        return 'accurate'
    else:
        return 'inaccurate'


def _training_model(model):

    return randint(1, 10)


with DAG("my_dag",
    start_date        = datetime(2021, 1 ,1), # start date, the 1st of January 2021
    schedule_interval = '@daily',             # Cron expression, here it is a preset of Airflow, @daily means once every day.
    catchup           = False                 # Catchup 
    ) as dag:

    training_model_tasks = [
        PythonOperator(
            task_id=f"training_model_{model_id}",
            python_callable=_training_model,
            op_kwargs={
                "model": model_id
            }
        ) for model_id in ['A', 'B', 'C']
    ]

    choosing_best_model = BranchPythonOperator(
        task_id         = "choosing_best_model",
        python_callable = _choosing_best_model
    )

    accurate = BashOperator(
        task_id      = "accurate",
        bash_command = "echo 'accurate'"
    )

    inaccurate = BashOperator(
        task_id      = "inaccurate",
        bash_command = "echo 'inaccurate'"
    )

    training_model_tasks >> choosing_best_model >> [accurate, inaccurate]