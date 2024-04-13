# Projeto de Previsão de Lucro

## 1. Descrição do Projeto
Este projeto visa desenvolver pipelines com os melhores parâmetros e hiper-parâmetros dos modelos de aprendizado de máquina para a escolha do melhor modelo para prever o lucro de vendas em um e-commerce. O modelo é treinado com um conjunto de dados fornecido pelo cliente, que inclui informações sobre vendas anteriores.

## Escolhas de Design
## Aplicação dos modelos de ML para tarefas de classificação:
#### Seleção de modelos:
* Regressão Logística
* Árvore de Decisão
* KNeighborsClassifier
* Random Forest.
* XG Boost


## Estrutura do Projeto
- `desafio.ipynb`: Este notebook contém todo o notebook com a análise, exploração, visualização dos dados
e elaboração dos modelos de previsão

## Como Executar
1. Instale as dependências com `pip install -r requirements.txt`.
2. Execute o notebook `desafio.ipynb` para rodar a análise, treinar o modelo e fazer as previsões.

## Avaliação
Foi utilizado as seguintes métricas para avaliar a previsão do modelo para o conjunto de validação: 
- Regressão Logística', 'Árvore de Decisão', 'KNN', 'Random Forest', 'XGBoost' 


# 2. MLFlow Experiment

Este projeto consiste em um experimento utilizando MLFlow para treinar e avaliar um modelo de classificação. O experimento foi dividido em diferentes etapas, cada uma delas separada em scripts/tasks.

## Estrutura do Projeto

O projeto está estruturado da seguinte forma:

- `extract_data.py`: Script responsável por extrair os dados brutos de uma fonte externa e salvá-los localmente.
- `transform_data.py`: Script responsável por carregar os dados brutos, realizar a transformação necessária (por exemplo, pré-processamento, feature engineering) e salvar os dados transformados.
- `mlflow_experiments.py`: Script para registrar os experimentos com MLflow.
- `train_model.py`: Script responsável por carregar os dados transformados, treinar o modelo utilizando GridSearchCV, salvar o modelo treinado e registrar métricas utilizando MLFlow.
- `predict_model.py`: Script responsável por carregar o modelo treinado, carregar os dados de teste, realizar a predição e avaliar o modelo utilizando as métricas desejadas.
- `mlruns/`: Diretório onde são armazenados os logs do MLFlow, incluindo parâmetros, métricas e artefatos dos experimentos.

## Como Executar

1. Certifique-se de ter instalado todas as dependências listadas no arquivo `requirements.txt`.
2. Usar o comando pip install -r requirements.txt para instalar todas as dependências listadas no arquivo. 
3. Execute o script `transform_data.py` para realizar a transformação dos dados brutos e salvar os dados transformados.
4. Execute o script `mlflow_experiments.py` para registrar os experimentos com MLflow antes de fazer o treinamento.
5. Execute o script `train_model.py` para treinar o modelo, salvar o modelo treinado e registrar as métricas.
6. Execute o script `predict_model.py` para carregar o modelo treinado, realizar a predição nos dados de teste e avaliar o modelo.

## Boas Práticas de Programação

- **Separação de Tarefas**: As diferentes etapas do experimento foram separadas em scripts individuais para melhor organização e reutilização de código.
- **Documentação**: Cada script contém comentários e documentação explicando sua funcionalidade e uso.
- **MLFlow**: Utilizei o MLFlow para rastrear e registrar todos os aspectos do experimento, incluindo parâmetros, métricas e artefatos.
- **README.md**: Foi criado um README.md explicando a estrutura do projeto, como executar os scripts e detalhes sobre as escolhas feitas.

## Contribuições e Problemas

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver alguma sugestão de melhoria, por favor, abra uma issue neste repositório.

