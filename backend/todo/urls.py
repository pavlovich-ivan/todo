# todo_list/todo_app/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
    path('list/', views.output_list, name='output_list'),
    path('list/create/', views.CreateTask.as_view(), name='create_list'),
]