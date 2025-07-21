from django.shortcuts import render
from django.views.generic import ListView,DetailView
from TasksApp.models import Task
from django import forms

class TaskListViews(ListView):
    model = Task
    template_name = 'TaskList.html'
    context_object_name = 'tasks'


class TaskDetailViews(DetailView):
    model = Task
    template_name = 'TaskDetail.html'
    context_object_name = 'task_info'



class Form()