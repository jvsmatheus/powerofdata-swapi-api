## Visão Geral
Esta API atua como um proxy da SWAPI (Star Wars API), permitindo
filtragem, ordenação e padronização de respostas, além de
autenticação via API Key.

Foi desenvolvida com foco em simplicidade, testabilidade e
pronta para deploy em Google Cloud Functions.

## Link base da cloud function

    https://us-central1-teste-swapi.cloudfunctions.net/swapi_api

## Arquitetura
A aplicação segue uma separação clara de responsabilidades:

- Controller: interpretação da requisição HTTP
- Service: regras de negócio
- Client: integração com a SWAPI
- Utils: filtros e ordenação
- Models: padronização de respostas
- Exceptions: erros controlados

## Tecnologias
- Python 3.12+
- Flask
- Pytest
- Requests
- Google Cloud Functions

## Configurações
A API utiliza variáveis de ambiente para configuração sensível.

Variáveis necessárias:

    API_KEY: sua-chave-aqui

## Execução local

1. Crie um ambiente virtual
2. Instale as dependências:

        pip install -r requirements.txt

3. Configure a variável de ambiente:

        export API_KEY=sua-chave-aqui  # Linux/Mac
        $env:API_KEY=sua-chave-aqui    # Windows powershell

4. Execute usando Functions Framework

## Testes
Os testes foram escritos com Pytest e cobrem:

- Autenticação
- Erros de negócio
- Filtragem
- Ordenação
- Integração simulada com a SWAPI (monkeypatch)

Para rodar os testes usar o comando

    pytest

## Autenticação
A API utiliza autenticação via header:

    x-api-key: <API_KEY>

## Endpoints
| Recurso       | Endpoint         | Filtros disponíveis             | Ordenação (`sort`)              |
| ------------- | ---------------- | ------------------------------- | ------------------------------- |
| **People**    | `/api/people`    | `name`, `gender`, `eye_color`   | `name`, `gender`, `eye_color`   |
| **Films**     | `/api/films`     | `title`, `director`, `producer` | `title`, `director`, `producer` |
| **Planets**   | `/api/planets`   | `name`, `climate`, `terrain`    | `name`, `climate`, `terrain`    |
| **Starships** | `/api/starships` | `name`, `model`, `manufacturer` | `name`, `model`, `manufacturer` |

## Exemplos de uso

    GET /api/people?gender=male  
    GET /api/people?name=luke&sort=name  
    GET /api/people?name=luke&sort=-name  # field_name -> asc; -field_name -> desc
    GET /api/films?director=lucas

### Fluxo da requisição

```text
HTTP Request
   ↓
Cloud Function (main)
   ↓
Controller (handle_request)
   ↓
Service (SwapiService)
   ↓
Client (SwapiClient)
   ↓
SWAPI

Retorno:
SWAPI → Client → Service → ApiResponse → HTTP Response