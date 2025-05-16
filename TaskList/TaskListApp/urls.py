from django.urls import path
from TaskListApp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add-task/', views.add_task, name='add_task'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
]