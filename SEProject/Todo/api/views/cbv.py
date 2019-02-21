from django.shortcuts import render, redirect
from main.models import List, Task
from main.forms import SearchForm, ListForm
from api.serializers import ListModelSerializer, TaskModelSerializer
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class ListsList(APIView):

    def get(self, request):
        lists = List.objects.all()
        serializer = ListModelSerializer(lists, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = ListModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListDetail(APIView):

    def get_object(self, pk):
        try:
            return List.objects.get(id=pk)
        except List.DoesNotExist:
            raise Http404

    def get(self, pk):
        list = self.get_object(pk)
        serializer = ListModelSerializer(list)
        return Response(serializer.data)

    def put(self, request, pk):
        list = self.get_object(pk)
        serializer = ListModelSerializer(instance=list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        list = self.get_object(pk)
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskList(APIView):

    def get(self, request):
        tasks = Task.objects.all()
        serializer = ListModelSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = TaskModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):

    def get_object(self, pk):
        try:
            return Task.objects.get(id=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, pk):
        task = self.get_object(pk)
        serializer = TaskModelSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskModelSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)