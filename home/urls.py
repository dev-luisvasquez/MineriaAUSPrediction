from django.contrib import admin
from django.urls import path
from .views import (predict, home)

urlpatterns = [
    path('', predict, name="predict"),
    
]


