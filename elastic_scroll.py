import pandas as pd
from elasticsearch import Elasticsearch

usuario = 'usuario'
senha = 'senha'

es = Elasticsearch('https://elasticsearch-saps.saude.gov.br',
                   http_auth=(usuario, senha), port=443)
index = 'esusve-go'

query = {
    "query":{
        "match_all":{}
    }
}
resultado = es.search(index=index,body=query, scroll='1m', size=10000)

sid = resultado['_scroll_id']
scroll_size = len(resultado['hits']['hits'])
dados = [dado['_source'] for dado in resultado['hits']['hits']]

while scroll_size > 0:
    resultado = es.scroll(scroll_id=sid, scroll='1m')
    sid = resultado['_scroll_id']

    scroll_size = len(resultado['hits']['hits'])
    dados += [dado['_source'] for dado in resultado['hits']['hits']]
    print(len(dados))

df = pd.DataFrame(dados)
df.to_csv('dados.csv', index=False)
