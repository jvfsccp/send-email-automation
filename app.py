import pandas as pd
from datetime import datetime
import time

from get_tickets import get_tickets
from url_taskid import url_taskid
from send_email import send_email

def main_loop():
    sent_ticket_ids = set()

    while True:
        status = '5'
        tickets = get_tickets(status)
        extracted_data_tickets = []
        new_tickets = []

        if tickets:
            for ticket in tickets:
                extracted_ticket = {
                    'id': ticket.get('id'),
                    'creationDate': ticket.get('creationDate'),
                    'title': ticket.get('title'),
                    'customerName': ticket.get('customerName'),
                    'statusType': ticket.get('statusType'),
                    'taskIds': ticket.get('taskIds'),
                    'endDate': ticket.get('endDate'),
                    'requesterEmail': str(ticket.get('requesterEmail'))
                }
                extracted_data_tickets.append(extracted_ticket)
                if ticket.get('id') not in sent_ticket_ids:
                    new_tickets.append(extracted_ticket)

            df_tickets = pd.DataFrame(extracted_data_tickets)
            print("Tickets encerrados:")
            print(df_tickets)
        else:
            print("Nenhum ticket encerrado encontrado na data e horário atual.")

        tasks = url_taskid()
        extracted_data_tasks = []

        if tasks:
            for task in tasks:
                if task.get('taskType') == 108332 and "CONFERIDO" in task.get('keyWordsDescriptions', []):

                    extracted_taskID = {
                        'taskID': task.get('taskID'),
                        'taskUrl': task.get('taskUrl'),
                        'taskType': task.get('taskType'),
                        'keyWords': task.get('keyWords'),
                        'keyWordsDescriptions': task.get('keyWordsDescriptions')
                    }
                    extracted_data_tasks.append(extracted_taskID)
            df_tasks = pd.DataFrame(extracted_data_tasks)
            print("Tarefas encontradas:")
            print(df_tasks)
        else:
            print("Nenhuma tarefa encontrada para os taskIDs dos tickets encerrados.")

        if new_tickets and extracted_data_tasks:
            send_email(new_tickets, extracted_data_tasks)
            for ticket in new_tickets:
                sent_ticket_ids.add(ticket['id'])

        print("Aguardando 30 segundos para a próxima atualização...")
        time.sleep(30)

if __name__ == "__main__":
    main_loop()