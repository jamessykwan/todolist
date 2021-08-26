from django.shortcuts import render
from django import forms
from .models import Task

tasks = Task.objects.all()

def home(request):
    return render(request, "todo/home.html", {
        "tasks": tasks
    })

def add_task(request):
    Task.objects.create(name='Task 2',content='hello')