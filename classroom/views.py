from django.shortcuts import render, redirect
from classroom.models import *
from django.shortcuts import render
from django.http import HttpResponse
from confluent_kafka import Producer

kafka_producer = Producer({
    'bootstrap.servers': 'localhost:9092',  
})

def send_kafka_message(req):
    if req.method == 'POST':
        try:
            kafka_producer.produce('MEY', key='your_key', value='your_message')
            kafka_producer.flush()
            print("เสร็จสิ้น")
            return render(req, 'classroom/one.html')
        except Exception as e:
            return HttpResponse(f"Error sending Kafka message: {str(e)}")
    return HttpResponse("Invalid request method.")

def page_one(req):
    return render(req, 'classroom/one.html')

def home(req):
    return render(req, 'classroom/home.html')

def page_two(req):
    return render(req, 'classroom/two.html')