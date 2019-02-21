from rest_framework import generics
from api.serializers import ListModelSerializer, TaskModelSerializer
from main.models import List, Task
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class IsSuperAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class IsStaff(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class GenericListList(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListModelSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return List.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class GenericListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListModelSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    lookup_field = 'list_id'

    def get_object(self):
        return List.objects.get(id=self.kwargs[self.lookup_field])

    def get_queryset(self):
        return List.objects.get(user=self)


class GenericTaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Task.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class GenericTaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    lookup_field = 'task_id'

    def get_object(self):
        return Task.objects.get(id=self.kwargs[self.lookup_field])

    def get_queryset(self):
        return Task.objects.for_user(self.request.user)