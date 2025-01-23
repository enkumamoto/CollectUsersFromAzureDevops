# Gerador de Relatório de Usuários e Licenças do Azure DevOps

Este script Python consulta a API do Azure DevOps para obter uma lista de usuários e suas respectivas licenças, gerando um arquivo CSV com essas informações.

## Requisitos

- Python 3.x
- Biblioteca `requests`
- Biblioteca `python-dotenv`

## Configuração

1. Instale as dependências necessárias executando:

   ```sh
   pip install requests python-dotenv
   ```

2. Crie um arquivo `.env` na mesma pasta do script e adicione suas credenciais:

   ```env
   PAT="GET_YOUR_PAT_ON_AZUREDEVOPS"
   AUTH_GRAPH_CLIENT_ID=""
   AUTH_GRAPH_SECRET=""
   AUTH_GRAPH_TENANT_ID=""
   ```

## Explicação do Código

1. O script carrega as variáveis de ambiente do arquivo `.env` usando `dotenv`.
2. Define as configurações da API do Azure DevOps, como a organização, versão da API e quantidade máxima de registros.
3. Constrói os cabeçalhos da requisição, incluindo a autenticação via token `PAT`.
4. Faz uma requisição HTTP `GET` para a API do Azure DevOps e verifica se a resposta foi bem-sucedida.
5. Caso os dados sejam retornados corretamente, ele extrai informações dos usuários, como:
   - Nome de exibição
   - Endereço de e-mail
   - Tipo de licença da conta
   - Nome da licença
   - Data do último acesso
6. Salva essas informações em um arquivo `user_license.csv`.
7. Se houver erros na requisição, exibe mensagens de erro.

## Execução

Para rodar o script, basta executar:

```sh
python CollectUsersFromAzureDevops.py
```

Isso gerará um arquivo `user_license.csv` contendo os dados dos usuários e suas licenças.

## Autor

Este script foi desenvolvido para facilitar a geração de relatórios de licenças de usuários no Azure DevOps.

---

# Azure DevOps Users and Licenses Report Generator

This Python script queries the Azure DevOps API to retrieve a list of users and their respective licenses, generating a CSV file with this information.

## Requirements

- Python 3.x
- `requests` library
- `python-dotenv` library

## Setup

1. Install the necessary dependencies by running:

   ```sh
   pip install requests python-dotenv
   ```

2. Create a `.env` file in the same folder as the script and add your credentials:

   ```env
   PAT=your_access_token
   PROJECT_ID=your_project_id
   ```

## Code Explanation

1. The script loads environment variables from the `.env` file using `dotenv`.
2. It defines the Azure DevOps API settings, such as the organization, API version, and maximum number of records.
3. It builds the request headers, including authentication via the `PAT` token.
4. It makes an HTTP `GET` request to the Azure DevOps API and checks if the response is successful.
5. If the data is returned correctly, it extracts user information such as:
   - Display Name
   - Email Address
   - Account License Type
   - License Display Name
   - Last Accessed Date
6. It saves this information in a `user_license.csv` file.
7. If there are errors in the request, it displays error messages.

## Execution

To run the script, simply execute:

```sh
python CollectUsersFromAzureDevops.py
```

This will generate a `user_license.csv` file containing the user and license data.

## Author

This script was developed to facilitate the generation of user license reports in Azure DevOps.

