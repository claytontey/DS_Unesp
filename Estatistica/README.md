# Exercícios


### Projeto de Classes 

Para esse conjunto de exercícios vamos utilizar o conjunto de dados
disponibilizado na API da NASA: [NeoWs (Near Earth Object Web Service)](https://api.nasa.gov/)

NeoWs (Near Earth Object Web Service) é um serviço da web RESTful para
informações de asteróides próximos à Terra. Com os NeoWs, um usuário pode:
pesquisar asteróides com base em sua data de aproximação mais próxima à Terra,
pesquisar um asteróide específico com sua identificação de corpo pequeno (small
body ID - NASA JPL), bem como navegar no conjunto de dados geral.


Utilizando a biblioteca [Pandas](https://pandas.pydata.org/), implemente
funções que realizem as seguintes tarefas:

#### Considerando os dados de avaliação dos usuários

1. Criar um dataset que contenha informações sobre os objetos próximos à terra,
   contendo informações das aproximações (esse deve ser um segundo `DataFrame`
   além do que contém informações básicas sobre os objetos);
  * Você deve fazer requisições às primeiras 100 páginas do Serviço;
1. Encontrar os seguintes dados:
  * Número de objetos perigosos a terra;
  * Distância média e desvio padrão entre objetos perigosos e a terra;
  * Histograma mostrando quantos objetos perigosos tiveram aproximações com a
    terra entre os anos 2000 e 2021 (agrupe os objetos por ano);
  * Histograma de tamanhos de objetos que são perigosos;
  * Histograma de tamanhos de objetos não perigosos;
