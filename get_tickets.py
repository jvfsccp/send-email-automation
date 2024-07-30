import requests
import json
import pandas as pd
from datetime import datetime


def get_tickets(status):
    # Chaves de API
    api_key = 'zXsSugfT2kgB6oAEMpTtQKDXvde8DQjX'
    api_token = 'zXsSugfT2kgLFDf1RgeTJW82sH9vIEM'

    # Solicitar token de autenticação
    login_url = 'https://api.auvo.com.br/v2/login/'
    headers = {
        'Content-Type': 'application/json'
    }
    params = {
        'apiKey': api_key,
        'apiToken': api_token
    }

    try:
        response = requests.get(login_url, headers=headers, params=params)
        response.raise_for_status()  # Verifica se a solicitação foi bem-sucedida
        token = response.json()['result']['accessToken']

        # Criar o token de autenticação Bearer
        auth_token = f'Bearer {token}'
        # Criar o filtro de parâmetros
        start_date = datetime.now().strftime('%Y-%m-%d')
        end_date = datetime.now().strftime('%Y-%m-%d')
        param_filter = json.dumps({
            "startDate": start_date,
            "endDate": end_date,
            "status": status,
            "SearchTasks": "true"
        })

        # URL para a solicitação dos tickets
        url_request = 'https://api.auvo.com.br/v2/tickets/'

        # Fazer a solicitação dos tickets
        params = {
            'paramFilter': param_filter,
            'page': '1',
            'pageSize': '100',
            'order': 'asc'
        }

        headers = {
            'Authorization': auth_token,
            'Content-Type': 'application/json'
        }

        response = requests.get(url_request, headers=headers, params=params)
        response.raise_for_status()  # Verifica se a solicitação foi bem-sucedida

        results = response.json()
        ticket = results['result']['entityList']
        return ticket

    except requests.exceptions.RequestException as e:
        print("Erro na solicitação:", e)
        return []

    except KeyError:
        print("Chave inválida encontrada na resposta da API")
        return []

    except json.JSONDecodeError:
        print("Erro ao decodificar a resposta JSON da API")
        return []

# Status para buscar os tickets encerrados
status = '5'
tickets = get_tickets(status)
# Create a list to store the extracted data
extracted_data = []
if tickets:
    # Iterate through each ticket and extract the desired columns
    for ticket in tickets:
        extracted_ticket = {
            'id': ticket.get('id'),
            'creationDate': ticket.get('creationDate'),
            'title': ticket.get('title'),
            'customerName': ticket.get('customerName'),
            'statusType': ticket.get('statusType'),
            'taskIds': ticket.get('taskIds'),
            'endDate': ticket.get('endDate'),
            'requesterEmail': ticket.get('requesterEmail'),
            'taskType': ticket.get('taskType')
        }
        extracted_data.append(extracted_ticket)

    # Create a pandas DataFrame from the extracted data
    df = pd.DataFrame(extracted_data)
    print(df)

else:
    print("Nenhum ticket encerrado encontrado na data e horário atual.")