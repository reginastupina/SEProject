from django.urls import path

from main import views

urlpatterns = [
    path('', views.show_lists, name='home'),
    path('<int:list>/todo', views.todo_list),
    path('<int:list>/completed', views.completed_todo_list),
    path('create_list', views.create_list),
    path('<int:fk>/delete_list', views.delete_list),
    path('<int:fk>/task_done/<int:pk>', views.make_done),
    path('<int:fk>/task_notdone/<int:pk>', views.make_notdone),
]