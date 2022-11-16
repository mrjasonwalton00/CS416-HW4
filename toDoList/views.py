from django.shortcuts import render
from django.http import HttpResponse

def toDoList(request):
    return render(request, 'toDoList/page1.html')

def page2(request):
    return render(request, 'toDoList/page2.html')
