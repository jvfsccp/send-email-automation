# Sistema de automação com python para envio de emails

## O que é cada arquivo?
- app.py é onde fica o meu looping infinito de atualizações
- send_email.py é o arquivo que irá realizar o envio de emails
- get_tickets.py é onde buscamos os tickets encerrados
- url_taskid.py é o arquivo responsável por me disponiblizar a task_url e taskID em lote dos tickets encerrados.

## Funcionalidades
- Busca o ticket com o status "encerrado";
- Com o ticket pela api temos o retorno de: email de cliente, nome do cliente, titulo e etc;
- Quando efetuar a busca do ticket, terá todas as tarefas relacionadas a ele;
- Encontrando essas tarefas, vamos buscar por tarefas especifícas relacionadas a esse ticket;
- Encontrando a url da tarefa, id de cada uma e o mais importante: a palavra-chave;
- Caso tenha a palavra-chave "CONFERIDO" em cada uma, o email será enviado automaticamente para o cliente informando que foi finalizado o ticket;
- Caso não tenha em todas, o email não será enviado;
- Atualiza de 1 em 1 hora na prática, porém aqui no repositório deixei de 30 em 30 segundos.

## História por trás
### Há mais ou menos 3 meses e meio meu chefe no meu estágio (na época) me perguntou se eu sabia fazer algum tipo de automação, respondi que não, porém me coloquei a disposição para fazer de qualquer forma. Ele me passou as instruções sobre o que seria e então comecei a desenvolver, está ai finalizada agora após 3 meses de desenvolvimento somente no horário de expediente quando sobrava algum tempinho em relação as outras tarefas.


<img src="https://user-images.githubusercontent.com/49786548/84605451-b6d36200-ae73-11ea-94b3-9927d07f85fd.png">
