from django.urls import path
from task import views



urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/create', views.task_create, name='task_form'),
    path('task/update/<int:pk>/', views.task_update, name='task_update'),
    path('task/delete/<int:pk>/', views.task_delete, name='task_delete'),
]