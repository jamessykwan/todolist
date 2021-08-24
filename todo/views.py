from django.shortcuts import render

tasks = Tasks.objects.all()

def home(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })