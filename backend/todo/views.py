from .serializers import ToDoItemCreateSerializer, ToDoItemSerializer
from .models import ToDoItem
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

@api_view(['GET'])
def output_list(request):
    tasks = ToDoItem.objects.all()
    serializer = ToDoItemSerializer(tasks, many=True)

    return Response(serializer.data)


class CreateTask(generics.GenericAPIView):
    serializer_class = ToDoItemCreateSerializer

    def post(self, request):
        serializer = ToDoItemCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return HttpResponseRedirect(redirect_to=reverse('output_list'))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)