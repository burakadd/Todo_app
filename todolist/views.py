from rest_framework import permissions, status, authentication
from rest_framework import generics
from rest_framework.response import Response

from todolist.models import Todo, MyUserModel
from todolist.serializers import TodoSerializer, UserSerializer


# Create your views here.

class TodoView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    model = Todo
    serializer_class = TodoSerializer

    def get_queryset(self):
        # raise Exception(self.request.user.id)
        return Todo.objects.filter(creator=self.request.user)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        Todo(creator=request.user, header=serializer.data['header']).save()
        return Response(request.data, status=status.HTTP_201_CREATED)


class TodoActionView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class CreateUserView(generics.CreateAPIView):
    model = MyUserModel
    serializer_class = UserSerializer
