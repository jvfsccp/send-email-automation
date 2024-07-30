# Sistema de automação com python para envio de emails

## O que é cada arquivo?
- app.py é onde fica o código para envio de email
- main_loop.py é o looping infinito para o envio (onde basicamente a automação vai ficar rodando durante o dia)
- get_tickets.py é onde buscamos os tickets encerrados
- url_taskid.py é o arquivo responsável por me disponiblizar a task_url e taskID em lote dos tickets encerrados.

## O que está dando errado?
- Pois então, você vai ver que estará tudo funcionando normalmente se você for no main loop e retirar essa parte do código, a parte que tem o conforme e o seu código:
- ![image](https://github.com/user-attachments/assets/00c9bc6d-b60e-4290-b8a0-2b5c0d4224b4)
- Infelizmente preciso conseguir buscar os tickets e tarefas encerradas com a keyWord "CONFORME" que tem o id de 124242, porém ela não é buscada com nenhum parametro que tentei.

## Por que é necessário o "CONFORME"?
- Pois essas tarefas e tickets que são encerradas com essa keyWord está tudo ok para ser enviado o email para o cliente, alegando que a tarefa foi finalizada corretamente.
- Sem o conforme, poderia vir com falhas na finalização ou alguma cagada de algum colaborador (risos).

### Ah, você pode mudar os emails lá para fazer o teste, tem dois emails meu lá mas pode mudar para o seu e sua senha também para dar certo.
