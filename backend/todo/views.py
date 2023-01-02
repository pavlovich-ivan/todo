from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.

class ToDoListViewSet(viewsets.ModelViewSet):
    queryset = ToDoList.objects.all().order_by('title')
    serializer_class = ToDoListSerializer

class ToDoItemViewSet(viewsets.ModelViewSet):
    queryset = ToDoItem.objects.all().order_by('title')
    serializer_class = ToDoItemSerializer