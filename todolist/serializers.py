from rest_framework import serializers
from .models import Todo, MyUserModel


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'header', 'completed',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUserModel
        fields = ('id', 'username', 'password',)

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = MyUserModel.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
