import pandas as pd
import mlflow

# Carregar o modelo treinado
model = mlflow.sklearn.load_model(r'C:\Users\allis\Downloads\MDCC\Untitled Folder\mlruns\0\e7142990b00c4716b9f71fbcf48362c6\artifacts\best_model')

# Carregar os dados de teste
X_test = pd.read_csv('transformed_X_test.csv')
y_test = pd.read_csv('transformed_y_test.csv')  # Substitua 'column_name' pelo nome da coluna alvo

# Fazer previsões
predictions = model.predict(X_test)

# Avaliar as previsões
test_score = model.score(X_test, y_test)
print("Test Score:", test_score)

# Salvar o resultado das previsões como artefato
pd.DataFrame(predictions).to_csv('predictions.csv', index=False)
mlflow.log_artifact('predictions.csv')

# Fim da execução do MLflow
mlflow.end_run()