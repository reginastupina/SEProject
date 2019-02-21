from django.urls import path
from api import views
from api.views import ListsList, ListDetail, GenericListList, GenericListDetail, TaskList, TaskDetail, GenericTaskList, GenericTaskDetail

urlpatterns = [
    path('login/', views.login),
    path('register/', views.register),
    path('list_cbv/', ListsList.as_view()),
    path('list_cbv/<int:pk>/', ListDetail.as_view()),
    path('list_fbv/', views.lists_list),
    path('list_fbv/<int:pk>/', views.lists_detail),
    path('list_gen/', GenericListList.as_view()),
    path('list_gen/<int:pk>/', GenericListDetail.as_view()),
    path('task_cbv/', TaskList.as_view()),
    path('task_cbv/<int:pk>/', TaskDetail.as_view()),
    path('task_fbv/', views.task_list),
    path('task_fbv/<int:pk>/', views.task_detail),
    path('task_gen/', GenericTaskList.as_view()),
    path('task_gen/<int:pk>/', GenericTaskDetail.as_view()),
]