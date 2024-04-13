import pandas as pd

def extract_data(data_path):
    # Carregar os dados
    data = pd.read_csv(data_path)
    return data

# Chamar a função de extração de dados
data = extract_data('dados.csv')

# Salvar os dados extraídos como um arquivo CSV
data.to_csv('extracted_data.csv', index=False)