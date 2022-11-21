from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate, DeleteView, TaskUpdate


urlpatterns = [
    path('', TaskList.as_view(), name = "tasks"),
    path('dummy/<int:pk>/', TaskDetail.as_view(), name = 'task'),
    path('task-create/', TaskCreate.as_view(), name = 'task-create'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name = 'task-delete'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name = 'task-update'),

    
    #path('add/', views.add, name = "add"),
    #path('update/', views.update, name = "update"),
    
    
    #path('dummy/', TaskList.as_view(), name = 'tasks'),
    #path('index/', views.index, name = "index"),
]