from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_todo, name='add_todo'),
    path('', views.todo_list, name='todo_list'),
]
