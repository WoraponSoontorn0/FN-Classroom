import time
import json
from django.shortcuts import render, redirect
from kafka import KafkaConsumer, KafkaProducer
from classroom.models import *

def get_message():
    consumer = KafkaConsumer('homework',
                             bootstrap_servers='localhost:9092',
                             consumer_timeout_ms=10000,
                             group_id='_id.hw')
    
    messages = []
    for msg in consumer:
        try:
            data = json.loads(msg.value)
            if 'message' in data and data['message'] != ':':
                messages.append(data['message'])
        except json.JSONDecodeError:
            pass

    consumer.close()
    return messages

def send_message(message):
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    time.sleep(1)
    producer.send('homework', {'message': message})
    producer.flush()
    producer.close()

def home(request):
    if request.method == 'POST':
        my_homework = request.POST.get('hw')
        send_message(my_homework)
        
    my_homework = get_message()
    return render(request, 'classroom/home.html', {'my_homework': my_homework})
