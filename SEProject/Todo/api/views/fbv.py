from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import ListModelSerializer, TaskModelSerializer
from main.models import List, Task


@api_view(['GET', 'POST'])
def lists_list(request, format=None):
    if request.method == 'GET':
        list = List.objects.all()
        serializer = ListModelSerializer(list, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ListModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def lists_detail(request, pk):
    try:
        list = List.objects.get(id=pk)
    except List.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ListModelSerializer(list)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ListModelSerializer(instance=list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def task_list(request, format=None):
    if request.method == 'GET':
        task = List.objects.all()
        serializer = TaskModelSerializer(task, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskModelSerializer(list)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskModelSerializer(instance=list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
