from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TodoSerializer, UserSerializer, CreateTodoSerializer
from .models import Todo

# Create your views here.


class TodoView(APIView):

    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        Todo.objects.create()
        return Response(status=201)

# class TodoView(viewsets.ModelViewSet):
#     serializer_class = TodoSerializer
#     queryset = Todo.objects.all()
#     permission_classes = (permissions.AllowAny,)


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer


class AddTodoView(CreateAPIView):
    model = Todo
    permission_classes = (permissions.AllowAny,)
    serializer_class = CreateTodoSerializer
