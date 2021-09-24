from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index),
    path('command/<int:id>/<cmd>', views.command),
]
