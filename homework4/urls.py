
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), #adds path to admin
    path('', include('toDoList.urls')), # adds path to toDolist/urls.py
]
