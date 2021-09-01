from .models import Task
from django import forms
from django.forms import ModelForm

class TaskForm(ModelForm):

    check_task = forms.BooleanField()

    class Meta:
        model = Task
        fields = '__all__'