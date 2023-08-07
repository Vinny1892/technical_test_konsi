## API 

A API foi desenvolvida utilizando o framework FastAPI, em conjunto com bibliotecas para acesso a serviços e gerenciamento de variáveis de ambiente.
Essa abordagem moderna e eficiente proporciona uma criação ágil e poderosa de APIs, permitindo um desenvolvimento mais produtivo e escalável. O FastAPI oferece recursos de documentação automática e validação de dados, facilitando a integração e o uso da API por outros sistemas e desenvolvedores. 


## Estrutura

A API foi estruturada com foco em desacoplar qualquer driver externo, seja fila ou banco de dados. Cada rota da API tem um serviço associado, que recebe as classes de repositório responsáveis pelo acesso ao banco de dados ou pela publicação na fila. No entanto, internamente, o serviço depende apenas de interfaces.

Essa abordagem de desacoplamento permite que a API seja mais flexível e adaptável a diferentes cenários e tecnologias. Ao depender apenas de interfaces internamente, os serviços não estão vinculados diretamente a implementações específicas de banco de dados ou sistemas de mensageria. Isso simplifica a manutenção e evolução da API, uma vez que é possível substituir facilmente as implementações das interfaces sem afetar a lógica interna dos serviços.

Além disso, a estrutura da API facilita a reutilização de código, pois os serviços podem ser compostos por diferentes repositórios que implementam as mesmas interfaces. Essa modularidade também torna os testes mais fáceis de serem realizados, uma vez que é possível criar mocks ou implementações de teste para as interfaces sem a necessidade de acessar recursos externos.

Em suma, a arquitetura desacoplada da API, com serviços e interfaces, contribui para um código mais limpo, organizado e adaptável, permitindo uma fácil manutenção e evolução da aplicação ao longo do tempo.

## Roadmap
  - [ ]  Diagrama C4 do fluxo da API