from sklearn.model_selection import StratifiedShuffleSplit, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import pandas as pd
import mlflow
import time

# Carregar os dados transformados
X = pd.read_csv('transformed_X.csv')
y = pd.read_csv('transformed_y.csv')

# Extracting values from DataFrame to ensure y is a 1D array
y = y.values.ravel()

# Dividir os dados em conjunto de treinamento e teste
splitter = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in splitter.split(X, y):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y[train_index], y[test_index]

# Salvar os dados de treinamento em CSV
X_train.to_csv('transformed_X_train.csv', index=False)
pd.DataFrame(y_train).to_csv('transformed_y_train.csv', index=False)

# Salvar os dados de teste em CSV
X_test.to_csv('transformed_X_test.csv', index=False)
pd.DataFrame(y_test).to_csv('transformed_y_test.csv', index=False)

# Iniciar uma execução do MLflow
mlflow.start_run()

# Iniciar o timer
start_time = time.time()

# Criar o pipeline
pipe = Pipeline([
    ('std_scaler', StandardScaler()),
    ('Logistic_Regression', LogisticRegression(max_iter=10000))
])

# Definir os parâmetros para pesquisa em grade
param_grid = [
    {'Logistic_Regression__solver': ['newton-cg', 'sag'],
     'Logistic_Regression__C': [0.1, 1.0, 10.0, 100.0],
     'Logistic_Regression__penalty': ['l2']},
    {'Logistic_Regression__solver': ['lbfgs'],
     'Logistic_Regression__C': [0.1, 1.0, 10.0, 100.0],
     'Logistic_Regression__penalty': ['l2']}
]

# Criar o objeto GridSearchCV
grid = GridSearchCV(pipe, param_grid, cv=5)

# Treinar o modelo
grid.fit(X_train, y_train)

# Calcular o tempo de execução
execution_time = time.time() - start_time
minutes, seconds = divmod(execution_time, 60)

# Registrar métricas no MLflow
mlflow.log_params(grid.best_params_)
mlflow.log_metrics({'best_score': grid.best_score_, 'execution_time_minutes': minutes, 'execution_time_seconds': seconds})

# Salvar o modelo treinado
mlflow.sklearn.log_model(grid.best_estimator_, "best_model")

# Avaliar o modelo com os dados de teste
test_score = grid.score(X_test, y_test)
mlflow.log_metric("test_score", test_score)

# Fim da execução do MLflow
mlflow.end_run()
