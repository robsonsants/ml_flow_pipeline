import mlflow
import os

# Iniciar uma execução do MLflow
mlflow.start_run()

# Salvar os dados extraídos como artefato
mlflow.log_artifact('extracted_data.csv')

# Salvar os dados transformados como artefatos
mlflow.log_artifact('transformed_X.csv')
mlflow.log_artifact('transformed_y.csv')

# Fim da execução do MLflow
mlflow.end_run()