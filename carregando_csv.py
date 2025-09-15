import pandas as pd

# Ignora a primeira linha de metadados
data_empresas = pd.read_csv('multiTimeline.csv', skiprows=1)

# Remove coluna isPartial se existir
if 'isPartial' in data_empresas.columns:
    data_empresas = data_empresas.drop(columns=['isPartial'])

# Converte primeira coluna para datetime
data_empresas[data_empresas.columns[0]] = pd.to_datetime(data_empresas[data_empresas.columns[0]], errors='coerce')

# Define como índice
data_empresas = data_empresas.set_index(data_empresas.columns[0])

# Remove linhas com datas inválidas
data_empresas = data_empresas.dropna()
print(data_empresas.head())
