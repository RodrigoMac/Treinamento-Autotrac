#include <iostream>
#include <SimpleAmqpClient/SimpleAmqpClient.h>

using namespace AmqpClient

int main()
{
    
    // ESTABELECER CONEXÃO COM RABBITMQ
    Channel::OpenOpts opts;
    opts.port = 5672; //Verificar porta do RabbitMQ na máquina
    opts.host = "localhost"; //Substituir localhost por IP
    opts.auth = Channel::OpenOpts::BasicAuth("espada", "@espada");
    
    Channel::ptr_t channel = Channel::Open(opts); 
    
    // PUBLICAR MENSAGEM
    BasicMessage::ptr_t myMessage = BasicMessage::Create("MENSAGEM QUALQUER");
    channel->BasicPublish("myExchange", "myRouting", myMessage); //Substituir myExchange pelo nome da Exchange, myRouting pela Routing Key ou pelo nome da Queue 
    
    // CONSUMIR MENSAGEM
    std::string consumer_tag = channel->BasicConsume("myQueue", ""); //Substituir myQueue pelo nome da Queue
    Envelope::ptr_t envelope = channel->BasicConsumeMessage(consumer_tag);

    return 0;
}