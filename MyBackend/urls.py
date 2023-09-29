from django.contrib import admin
from django.urls import path, include
from classroom.models import *
from classroom.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('classroom.urls')),
]
