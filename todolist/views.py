from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from .serializers import TodoSerializer, UserSerializer
from .models import Todo

# Create your views here.


class TodoView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    model = Todo
    # queryset = Todo.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TodoSerializer

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(creator=user)


class TodoActionView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class CreateUserView(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
