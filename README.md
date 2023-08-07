# API Scrap Beneficio


## Descrição

O projeto esta separado na api rest e no etl feito para fazer scarp dos dados


## 💻 Pré-requisitos

  

Antes de começar, verifique se você atendeu aos seguintes requisitos:

* docker `^20.10.8`
* docker-compose `^2.19.1`


  

<br>

  

## 🚀 Instalação
 o arquivo de .env é utilizado para popular as variaveis necessarias para aplicação se conectar com serviços externos necessarios e funcionar corretamente. Para utilização com o docker-compose-common não é necessario nenhuma mudança nos valores presente .env.example.
   Caso seja a primeira vez subindo o serviço entrar na pasta da api ou do crawler_benefit e rodar os seguintes comandos.
     - make init
     - make create-elasticsearch-index
 No caso do ocorrer erro no ultimo comando aguarde alguns segundos e então execute novamente, esse erro aconteçe porque pode ser que o elasticsearch ainda não esteja iniciado totalmente.  
<br>

  

  

### Clone este repositório usando ssh ou https

````

$ git clone git@github.com:Vinny1892/technical_test_konsi.git

````

#### Acesse a pasta do projeto no terminal/cmd

```

$ cd technical_test_konsi

```

  

<br>

  

### Para fazer build da imagem docker:

 acessar a pasta  technical_test_konsi/api/ ou a pasta technical_test_konsi/etl/crawler_benefit. podendo usar o build para producão e desenvolvimento

```docker

$ docker build -f docker/development/dockerfile -t user/name-image

```

Aonde:

* User = Usuario dockerhub

* Name-image = Nome da imagem

  
  

<!-- Para instalar o projeto , siga estas etapas: -->

  
<br>

  

#### Executa a aplicação em modo desenvolvimento

  

```

$ docker-compose up -d

```


## Execução dos testes e fixtures

Para execução dos testes e de outros comandos de forma simplificada no perojeto foi criado um `Makefile`, para rodar os testes só precisa rodar
```
make up-silent
make test
```



## 🛠 Tecnologias

  

As seguintes serviços foram usados na construção do projeto:

  
- [Selenium](https://www.selenium.dev/)

- [RabbitMQ](https://www.rabbitmq.com/)

- [elasticsearch](https://www.elastic.co/pt/)

- [redis](https://redis.io/)



## Endpoints

 Após instalado a aplicação pode-se acessar os recursos listados abaixo
   - buscar um beneficio que ja foi feito webscrap
   - fazer webscrap de um beneficio

### fazer webscrap de um beneficio

POST  http://localhost:32568/benefit com o body abaixo

```json

{
	"cpf": "<cpf para buscar o numero do beneficio>",
	"login": "usuario na plataforma",
	"password": "senha na plataforma"
}
````
também pode utilizar com o curl dessa forma.
```bash

curl -X POST -H "Content-Type: application/json" -d '{
	"cpf": "<cpf para buscar o numero do beneficio>",
	"login": "usuario na plataforma",
	"password": "senha na plataforma"
}' http://localhost:32568/benefit


`````
###  buscar um beneficio que ja foi feito webscrap

 Utilizar um get com o cpf que tem o numero atrelado ao beneficio

GET  http://localhost:32568/benefit/cpf 
também pode utilizar com o curl dessa forma.
```bash

curl -X GET -H "Content-Type: application/json" http://localhost:32568/benefit/<cpf>

`````

# Arquitetura
   - [ETL CRAWLER BENEFICIO](./etl/crawler_benefit/README.md)
   - [API](./api/README.md)