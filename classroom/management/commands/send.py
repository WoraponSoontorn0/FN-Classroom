from kafka import KafkaProducer
import json

def send_to_kafka(mensagem):
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    producer.send('topico_teste', {'mensagem': mensagem})
    producer.flush()
    producer.close()
