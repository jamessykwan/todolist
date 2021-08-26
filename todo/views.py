from django.shortcuts import render
from django import forms
from .models import Task

tasks = Task.objects.all()

def home(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            name = request.POST.get('title')
            content = request.POST.get('content')
            add_task(name,content)

    return render(request, "todo/home.html", {
            "tasks": tasks 
            })

def add_task(task_name, task_content):
    Task.objects.create(name=task_name, content=task_content)

def clear_tasks(request):
    Task.objects.all().delete()
    return render(request, "todo/home.html", {
            "tasks": tasks
        })



   
