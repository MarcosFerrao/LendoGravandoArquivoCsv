import csv
import requests
import pandas as pd
from config import URL, ARQUIVO_CSV


# Requisição para o link do arquivo .csv
response = requests.get(URL)
# print(response.content)

# Criando arquivo 'covid19.csv' e salvando no pc local
with open('covid19.csv', 'w', newline='\n') as novo_arquivo:
    writer = csv.writer(novo_arquivo)
    for linha in response.iter_lines():
        writer.writerow(linha.decode('utf-8').split(','))

# # Abrir um arquivo a partir do projeto raiz
# with open(ARQUIVO_CSV) as arquivo:
#     leitor_exemplo = csv.reader(arquivo)
#     for linha in leitor_exemplo:
#         # print(linha)
#         # if linha[2] == 'Brazil' and linha[3] == '2020-04-09':
#         #     print(f"Linha # {leitor_exemplo.line_num} {linha}")
#         if linha[2] == 'Brazil':
#             print(f"Linha # {leitor_exemplo.line_num} {linha}")

# # Mostra o arquivo inteiro
# arquivo_csv = pd.read_csv(ARQUIVO_CSV)

# # Mostra o arquivo csv porinteiro
# print(arquivo_csv.head().to_string())

# # Mostra o arquivo iniciando pelos ultimos dados com .tail() e desde o inicio com .head()
# print(arquivo_csv['continent'].tail())
# print(arquivo_csv['continent'].head())

# Usando o módulo pandas para ler o arquivo cvs
arquivo_csv = pd.read_csv(ARQUIVO_CSV, usecols=['location', 'date', 'total_cases', 'total_deaths'], index_col='date')

# Mostrando os 10 primeiros arquivos
# print(arquivo_csv.head(10).to_string())

# Filtrando dados
print(arquivo_csv.loc[(arquivo_csv.location == 'Brazil') & (arquivo_csv.index == '2021-05-05')])