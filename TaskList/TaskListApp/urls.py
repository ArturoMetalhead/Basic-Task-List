from django.urls import path
from TaskListApp import views

urlpatterns = [
    path('',views.home,name='home'),
]