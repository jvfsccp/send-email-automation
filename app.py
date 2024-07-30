import pandas as pd
from datetime import datetime, timedelta
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from get_tickets import get_tickets 
from url_taskid import url_taskid


def send_email(tickets, tasks):
    status = '5'
    tickets = get_tickets(status)
    extracted_data = []
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
                'requesterEmail': ticket.get('requesterEmail')
            }
            extracted_data.append(extracted_ticket)

    tasks = url_taskid()
    extracted_data_ticket = []
    if tasks:
        for task in tasks:
             if task.get('taskType') == 108332:
                extracted_taskID = {
                'taskID': task.get('taskID'),
                'taskUrl': task.get('taskUrl'),
                'taskType': task.get('taskType')
            }
                extracted_data_ticket.append(extracted_taskID)

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "joaovictorfernandescastro@gmail.com"
    smtp_password = "vujc gtmy arbp ufmx"

    requester_email = 'joaovfernandescastro@gmail.com'
    if extracted_data and extracted_data_ticket:
        ticket = extracted_data[0]
        task = extracted_data_ticket[0]
        for ticket, task in zip(tickets, tasks):
            subject = f"{ticket['title']} ENCERRADO"
            body = f"""
            O ticket com o ID {ticket['id']} foi encerrado.
            Título: {ticket['title']}
            Tipo de Tarefa: Corretiva
            Status: Encerrado
            Task IDs: {ticket['taskIds']}
            Data de encerramento: {ticket['endDate']}
            Relatório da tarefa: {task['taskUrl']}
            """

        msg = MIMEMultipart()
        msg['From'] = smtp_username
        msg['To'] = requester_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)
            text = msg.as_string()
            server.sendmail(smtp_username, requester_email, text)
            server.quit()
            print(f"Email enviado para {requester_email} com sucesso.")
        except Exception as e:
            print(f"Erro ao enviar email: {e}")

# Chame a função fora dela mesma
try:
    send_email(None, None)  # Passe os valores adequados para a função
except Exception as e:
    print(f"Erro ao enviar email: {e}")
