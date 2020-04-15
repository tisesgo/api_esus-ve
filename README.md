### Descrição
Código Python que consulta a API disponibilizada pelo Ministério da Saúde para consultar os casos notificados de COVID-19 no sistema [e-SUS VE](https://notifica.saude.gov.br/login "e-SUS VE").

O arquivo **elastic.py** busca até 10.000 registros. Para buscar mais registros usar o arquivo **elastic_scroll.py**.

Para executar o código basta colocar seu usuário, senha e alterar o index para a sigla do seu Estado. O index do estado de São Paulo ficaria:
> index = 'esusve-sp'

### Utilização
O código foi feito para rodar em Python3, utilizando a distribuição [Anaconda](https://www.anaconda.com/ "Site da distribuição Anaconda").

### Desenvolvido pela equipe de Gerência de Inovação da SES-GO
e-mail: inovacao.saude@goias.gov.br
