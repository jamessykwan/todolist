from django.shortcuts import render,redirect
from django import forms
from .models import Task

tasks = Task.objects.all()

def home(request):
    tasks = Task.objects.all()
    return render(request, "todo/home.html", {
        "tasks": tasks
    })


def addTask(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            name = request.POST.get('title')
            content = request.POST.get('content')
            add_task(name, content)
            return redirect('home')
    return render(request, "todo/addTask.html", {
        "tasks": tasks
    })


def add_task(task_name, task_content):
    Task.objects.create(name=task_name, content=task_content)


def clear_tasks(request):
    Task.objects.all().delete()
    return redirect('home')
