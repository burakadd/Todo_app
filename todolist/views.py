from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .serializers import TodoSerializer, UserSerializer
from .models import Todo

# Create your views here.


class TodoView(generics.ListCreateAPIView):
    model = Todo
    queryset = Todo.objects.all()
    permission_classes = (permissions.AllowAny,)
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TodoSerializer


class TodoActionView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class CreateUserView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
