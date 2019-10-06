from rest_framework import permissions, status
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from .serializers import TodoSerializer, UserSerializer
from .models import Todo, MyUserModel

# Create your views here.


class TodoView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication,]
    model = Todo
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TodoSerializer

    def get_queryset(self):
        # raise Exception(self.request.user.id)
        return Todo.objects.filter(creator=self.request.user)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=
            status.HTTP_400_BAD_REQUEST)
        else:
            todo = Todo(creator=request.user, header=serializer.data['header'],)
            todo.save()
            return Response(request.data, status=status.HTTP_201_CREATED)

class TodoActionView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class CreateUserView(generics.CreateAPIView):
    model = MyUserModel
    serializer_class = UserSerializer
