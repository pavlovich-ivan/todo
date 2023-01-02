from django.contrib import admin
from todo.models import ToDoItem, ToDoList

# Register your models here.

admin.site.register(ToDoItem)
admin.site.register(ToDoList)