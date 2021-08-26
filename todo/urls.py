from django.urls import path
from todo import views

urlpatterns = [
    path("", views.home, name="home"),
    path("clear/", views.clear_tasks, name="clear"),
    path("addTask/", views.addTask, name="addTask")
]