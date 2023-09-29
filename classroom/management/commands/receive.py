from kafka import KafkaConsumer
import json 

def receive_from_kafka():
    consumer = KafkaConsumer(
        'topico_teste',
        bootstrap_servers='localhost:9092',
        consumer_timeout_ms=1000,
        group_id='grupo.teste'
    )
    for msg in consumer:
        mensagem = json.loads(msg.value.decode('utf-8'))
    consumer.close()
