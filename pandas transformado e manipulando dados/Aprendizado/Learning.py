import pandas as pd
import requests
import numpy as np

url_hospedagem = 'C:\\Users\\Marcio\\Desktop\\python_Alura\\pandas transformado e manipulando dados\\Objetos Json\\dados_hospedagem.json'
url_moveis = 'C:\\Users\\Marcio\\Desktop\\python_Alura\\pandas transformado e manipulando dados\\Objetos Json\\moveis_disponiveis.json'
dados = pd.read_json(url_hospedagem)
dados.head()

dados = pd.json_normalize(dados['info_moveis'])
dados.head()

colunas = list(dados.columns)
print(colunas)
dados = dados.explode(colunas[3:])
print(dados)

dados.reset_index(inplace=True,drop=True)
dados.head()

dados.info()

dados['max_hospedes'] = dados['max_hospedes'].astype(np.int64)
dados.info()

col_numericas = ['quantidade_banheiros', 'quantidade_quartos','quantidade_camas']
dados[col_numericas] = dados[col_numericas].astype(np.int64)
dados['avaliacao_geral'] = dados['avaliacao_geral'].astype(np.float64)
dados.info()

dados[['preco','taxa_limpeza','taxa_deposito']] = dados[['preco','taxa_limpeza','taxa_deposito']].applymap(lambda x : x.replace('$', '').replace(',','').strip()) # type: ignore
dados[['preco','taxa_limpeza','taxa_deposito']] = dados[['preco','taxa_limpeza','taxa_deposito']].astype(np.float64)


dados.head()

print(dados)