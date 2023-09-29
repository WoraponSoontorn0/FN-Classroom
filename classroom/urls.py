from django.urls import path
from classroom import views

urlpatterns = [
     path('', views.home, name="home"),
     path('page_one/', views.page_one, name='page_one'),
     path('page_two/', views.page_two, name='page_two'),
     path('send_kafka_message/', views.send_kafka_message, name='send_kafka_message'),
]
