import pandas as pd
from elasticsearch import Elasticsearch
usuario = 'usuario'
senha = 'senha'
es = Elasticsearch('https://elasticsearch-saps.saude.gov.br',
                   http_auth=(usuario, senha), port=443)
index = 'esusve-go'
query = {
    "size": 10000,
    "query": {
        "match_all": {}
    }
}
resultado = es.search(index=index, body=query)['hits']['hits']
dados = [dado['_source'] for dado in resultado]

df = pd.DataFrame(dados)
df.to_csv('dados.csv', index=False)
