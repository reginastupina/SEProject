from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from api.serializers import UserModelSerializer
from django.contrib.auth.models import User
from rest_framework import status


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'Invalid data'})

    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})


@api_view(['POST'])
def register(request):
    serializer = UserModelSerializer(data=request.data)
    if serializer.is_valid():
        User.objects.get(
            request.data.get('username'),
            request.data.get('email'),
            request.data.get('password')
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

