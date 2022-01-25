# CRIAR UMA FILA TESTE E MANDAR UMA MENSAGEM PARA A FILA

import pika
import logging

FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

logging.getLogger('pika').propagate = False

# DEFINE OS PARAMETROS DE CONEXAO COM O RABBITMQ Credentials(usuario, senha); Parameters('localhost', 5672, '/', credentials)
credentials = pika.PlainCredentials('espa', '@espada')
parameters = pika.ConnectionParameters('localhost',
                                       5672,
                                       '/',
                                       credentials)

logging.info('Creating connection')

# CRIA CONEXAO COM SERVIDOR DO RABBITMQ
try:
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # CRIA UMA FILA DE TESTE NO RABBITMQ
    channel.queue_declare('TesteRodrigo')

    # DEFAUTL EXCHANGE: ENVIA MENSAGEM PARA FILA COM NOME IGUAL A ROUTING KEY
    channel.basic_publish('', 'TesteRodrigo', 'ALOW2')

    # ENCERRA CONEXAO
    connection.close()

except pika.exceptions.ProbableAuthenticationError as error:
    logging.error(error)
