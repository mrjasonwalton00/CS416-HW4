from django.urls import path
from . import views


urlpatterns = [
    path('', views.toDoList, name = "toDoList"),
    path('page2/', views.page2, name = "page2"),
]