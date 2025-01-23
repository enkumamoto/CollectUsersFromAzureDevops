import requests
import os
import base64
import csv
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

ORGANIZATION = "corpname"
PAT = os.getenv('PAT')
API_VERSION = "7.1-preview.1"
PROJECT_ID = os.getenv("PROJECT_ID")
MAX = 2000

# Verificar se as variáveis de ambiente foram carregadas corretamente
if not PAT or not PROJECT_ID:
    raise ValueError(
        "PAT ou PROJECT_ID não foram definidos nas variáveis de ambiente.")

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Basic {base64.b64encode(f":{PAT}".encode("utf-8")).decode("utf-8")}'
}

url = f"https://vsaex.dev.azure.com/{ORGANIZATION}/_apis/userentitlements?top={MAX}&api-version={API_VERSION}"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()

    if 'value' in data:
        # Abre o arquivo CSV para escrita
        with open('user_license.csv', 'w', newline='', encoding='utf-8') as csvfile:
            # Define os cabeçalhos do CSV
            fieldnames = ['Display Name', 'Mail Address',
                          'Account License Type', 'License Display Name', 'Last Accessed Date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Escreve o cabeçalho no arquivo CSV
            writer.writeheader()

            for item in data['value']:
                user = item.get('user')
                access_level = item.get('accessLevel')

                if user:
                    display_name = user.get('displayName')
                    mail_address = user.get('mailAddress')

                    if access_level:
                        account_license_type = access_level.get(
                            'accountLicenseType')
                        license_display_name = access_level.get(
                            'licenseDisplayName')
                    else:
                        account_license_type = None
                        license_display_name = None

                    last_accessed_date = item.get('lastAccessedDate')

                    # Escreve a linha no arquivo CSV
                    writer.writerow({
                        'Display Name': display_name,
                        'Mail Address': mail_address,
                        'Account License Type': account_license_type,
                        'License Display Name': license_display_name,
                        'Last Accessed Date': last_accessed_date
                    })
                else:
                    print("Chave 'user' não encontrada neste item!")
        # mensagem de sucesso
        print("Arquivo CSV 'result.csv' criado com sucesso.")
    else:
        print("Chave 'value' não encontrada no JSON!")
else:
    print(f"Erro na requisição: {response.status_code} - {response.text}")