import pandas as pd
import numpy as np

locacao_url = '/content/drive/MyDrive/Ciência de Dados/Data Science Alura/dados_locacao_imoveis.json'
data_locacao = pd.read_json(locacao_url)
data_locacao = pd.json_normalize(data_locacao['dados_locacao'])
data_locacao.head()

columns = list(data_locacao.columns)
data_locacao = data_locacao.explode(columns[1:])
print(data_locacao)

data_locacao.reset_index(drop=True,inplace=True)

data_locacao['valor_aluguel'] = data_locacao['valor_aluguel'].apply(lambda x : x.replace('$','').replace(',','.').replace('reais',''))
data_locacao['valor_aluguel'] = data_locacao['valor_aluguel'].astype(np.float64)
data_locacao.head()

data_locacao['apartamento'] = data_locacao['apartamento'].str.replace(' \(blocoAP\)', ' ',regex=True)
data_locacao.head()

data_locacao['datas_combinadas_pagamento'] = pd.to_datetime(data_locacao['datas_combinadas_pagamento'], format='%d/%m/%Y')
data_locacao['datas_de_pagamento'] = pd.to_datetime(data_locacao['datas_de_pagamento'], format='%d/%m/%Y')
data_locacao.head()

data_locacao['atraso'] = (data_locacao['datas_de_pagamento'] - data_locacao['datas_combinadas_pagamento']).dt.days

media_atraso = data_locacao.groupby(['apartamento'])['atraso'].mean()
media_atraso