import pandas as pd
import numpy as np

def transform_data(data_path):
    # Carregar os dados extraídos
    data = pd.read_csv(data_path)
    
    # 1. Análise e Exploração dos Dados
    data['Taxa_Lucro'] = data['Profit'] / data['Sales']
    X = data.drop(['Profit', 'Taxa_Lucro'], axis=1)
    y = (data['Profit'] < 0).astype(int)
    
    # Codificação One-Hot
    X_encoded = pd.get_dummies(X)
    
    return X_encoded, y

# Chamar a função de transformação de dados
X_encoded, y = transform_data('extracted_data.csv')

#é necessário fazer essa transformação
y = np.ravel(y)
#y = y.values.reshape(-1,)



# Salvar os dados transformados como arquivos CSV
X_encoded.to_csv('transformed_X.csv', index=False)
pd.DataFrame(y, columns=['Profit']).to_csv('transformed_y.csv', index=False)
#y_df.to_csv('transformed_y.csv', index=False)