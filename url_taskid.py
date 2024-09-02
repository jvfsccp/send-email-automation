import requests
import json
import pandas as pd
from datetime import datetime



def url_taskid():
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = datetime.now().strftime('%Y-%m-%d')

        # Chaves de API
        api_key = 'sua api key'
        api_token = 'sua api token'

        # Solicitar token de autenticação
        login_url = 'url para gerar a autenticação'
        headers = {
            'Content-Type': 'application/json'
        }
        params = {
            'apiKey': api_key,
            'apiToken': api_token
        }

        response = requests.get(login_url, headers=headers, params=params)
        response.raise_for_status()  # Verifica se a solicitação foi bem-sucedida
        token = response.json()['result']['accessToken']

        # Criar o token de autenticação Bearer
        auth_token = f'Bearer {token}'

        # Criar o filtro de parâmetros para buscar as tarefas correspondentes aos taskIDs dos tickets encerrados
        param_filter = json.dumps ({
            "startDate":start_date,
            "endDate":end_date,
            "status":"5",
            "SearchTasks":"true"
        })

        # URL para a solicitação das tasks
        url_request = 'url para o request'

        params = {
            'paramFilter': param_filter,
            'page': '1',
            'pageSize': '100',
            'order': 'asc'
          }


        headers['Authorization'] = auth_token

        response = requests.get(url_request, headers=headers, params=params)
        response.raise_for_status()  # Verifica se a solicitação foi bem-sucedida

        results = response.json()
        tasks = results['result']['entityList']

        return tasks


tasks = url_taskid()

extracted_data = []
if tasks:
    for task in tasks:
        if task.get('taskType') == 108332 and "CONFORME" in task.get('keyWordsDescriptions', []):
            extracted_taskID = {
            'taskID': task.get('taskID'),
            'taskUrl': task.get('taskUrl'), 
            'keyWords': task.get('keyWords'),
            'keyWordsDescriptions': task.get('keyWordsDescriptions')
            }
            extracted_data.append(extracted_taskID)

            df = pd.DataFrame(extracted_data)
            print(df)
else:
    print("Nenhuma tarefa encontrada para os taskIDs dos tickets encerrados.")
