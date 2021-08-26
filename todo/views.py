from django.shortcuts import render
from django import forms
from .models import Task

tasks = Task.objects.all()


def home(request):
     if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            post = Task()
            post.name = request.POST.get('title')
            post.content = request.POST.get('content')
            post.save()
            tasks = Task.objects.all()

            return render(request, "todo/home.html", {
                "tasks": tasks
            })

     else:
        tasks = Task.objects.all()

        return render(request, "todo/home.html", {
            "tasks": tasks
        })


def add_task(request):
    Task.objects.create(name='Task 2', content='hello')



   
