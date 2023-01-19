# serializers.py
from rest_framework import serializers
from .models import *

class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ('id', 'title', 'due_date','completed', 'important')



class ToDoItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ('title', 'due_date', 'important')
