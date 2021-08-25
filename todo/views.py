from django.shortcuts import render
from .models import Task

tasks = Task.objects.all()

def home(request):
    return render(request, "todo/home.html", {
        "tasks": tasks
    })