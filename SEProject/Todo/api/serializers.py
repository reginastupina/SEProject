from rest_framework import serializers
from main.models import List, Task
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=300)
    email = serializers.EmailField()
    is_staff = serializers.BooleanField()


class ListModelSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = List
        fields = ['id', 'name', 'created_by']


class TaskModelSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    list_id = ListModelSerializer(read_only=True)

    class Meta:
        model = List
        fields = ['id', 'name', 'owner', 'cd_date', 'due_date', 'mark', 'list_id']


class UserModelSerializer(serializers.ModelSerializer):

     class Meta:
         model = User
         field = ['id', 'username', 'password', 'email']
