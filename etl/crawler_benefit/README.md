## Crawle Benefit
 
O processo ETL foi implementado em Python, utilizando bibliotecas para acessar serviços e gerenciar variáveis de ambiente. Sua estrutura opera com base em um sistema de escuta à fila do RabbitMQ ao iniciar a aplicação. Quando uma nova mensagem é recebida, o consumidor processa a busca pelo número de benefício e, ao final, armazena os resultados no Redis e Elasticsearch.

Esse fluxo permite a ingestão, transformação e carga de dados de forma assíncrona, aproveitando as funcionalidades de mensageria do RabbitMQ para lidar com a transferência de informações entre componentes de maneira eficiente. O Redis e o Elasticsearch são utilizados como bancos de dados para armazenar e indexar os dados processados, proporcionando uma rápida recuperação de informações para consultas posteriores.

Esse processo ETL automatizado e ágil é fundamental para manter a consistência e a atualização dos dados utilizados no sistema.


## Estrutura
A estrutura foi projetada com um alto nível de desacoplamento, permitindo que o driver de consumo da fila do RabbitMQ funcione de forma independente. O consumidor é projetado para não depender diretamente da fila utilizada para o consumo, tornando-o mais flexível e adaptável a diferentes cenários de uso.

Internamente, o consumidor utiliza uma estrutura baseada no padrão de projeto Template Method. Essa abordagem padroniza a execução da pipeline, permitindo a fácil adaptação e mudança de qualquer um dos estágios do processo, sem comprometer o fluxo geral da aplicação.

Essa flexibilidade torna a estrutura mais robusta e facilita a manutenção e evolução do sistema ao longo do tempo. À medida que novos requisitos ou tecnologias surgem, a estrutura desacoplada e baseada no padrão Template Method possibilita a adição e substituição de etapas do processo com relativa facilidade, sem impactar negativamente o funcionamento geral do consumidor e da pipeline. Isso resulta em um código mais limpo, modular e com maior capacidade de adaptação a mudanças futuras.


## Roadmap
  - [ ]  Diagrama C4 do fluxo do ETL
  - [ ]  Mandar logs para elastisearch