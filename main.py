# CRIAR UMA FILA TESTE E MANDAR UMA MENSAGEM PARA A FILA

import pika
import logging
import pyodbc

def on_message(channel, method, properties, body):
    logging.info(f'Received message: {body}')
    if body == b'stop':
        raise KeyboardInterrupt("")

cnxn = connection = pyodbc.connect(f'DRIVER=ODBC Driver 17 for SQL Server;SERVER=localhost\SQLSERVER,1433;DATABASE=Treinamento;UID=espada;PWD=@espada')

cursor = cnxn.cursor()

#trocar message por body, timestamp por data atual
cursor.execute("insert into Message(text, timestamp) values ('ALOW', '1972-12-10 18:41:39')")
cnxn.commit()

FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

logging.getLogger('pika').propagate = False

# DEFINE OS PARAMETROS DE CONEXAO COM O RABBITMQ Credentials(usuario, senha); Parameters('localhost', 5672, '/', credentials)
credentials = pika.PlainCredentials('espada', '@espada')
parameters = pika.ConnectionParameters('localhost',
                                       5672,
                                       '/',
                                       credentials)

logging.info('Creating connection')

# CRIA CONEXAO COM SERVIDOR DO RABBITMQ
try:
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # BASIC GET
    #method, properties, body = channel.basic_get('TesteRodrigo', auto_ack=True)

    # CONSUME
    channel.basic_consume('TesteRodrigo', on_message, auto_ack=True)

    channel.start_consuming()

    # CRIA UMA FILA DE TESTE NO RABBITMQ
    # channel.queue_declare('TesteRodrigo')

    # DEFAUTL EXCHANGE: ENVIA MENSAGEM PARA FILA COM NOME IGUAL A ROUTING KEY
    #channel.basic_publish('', 'TesteRodrigo', 'ALOW2')

    # ENCERRA CONEXAO

except KeyboardInterrupt:
    logging.info("Get KeyboardInterrupt")
    channel.stop_consuming()
    connection.close()

