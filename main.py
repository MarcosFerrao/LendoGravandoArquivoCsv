import csv
import requests
from config import URL, ARQUIVO_CSV


# Requisição para o link do arquivo .csv
response = requests.get(URL)
# print(response.content)

# Criando arquivo 'covid19.csv' e salvando no pc local
with open('covid19.csv', 'w', newline='\n') as novo_arquivo:
    writer = csv.writer(novo_arquivo)
    for linha in response.iter_lines():
        writer.writerow(linha.decode('utf-8').split(','))

# Abrie um arquivo a partir do projeto raiz
with open(ARQUIVO_CSV) as arquivo:
    leitor_exemplo = csv.reader(arquivo)
    for linha in leitor_exemplo:
        # print(linha)
        # if linha[2] == 'Brazil' and linha[3] == '2020-04-09':
        #     print(f"Linha # {leitor_exemplo.line_num} {linha}")
        if linha[2] == 'Brazil':
            print(f"Linha # {leitor_exemplo.line_num} {linha}")