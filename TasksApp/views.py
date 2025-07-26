from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from TasksApp.models import Task
from django.urls import reverse_lazy
from TasksApp.forms import TaskForm
from django.contrib.auth.mixins import  LoginRequiredMixin
from TasksApp.mixins import UserIsOwnerMixin

class TaskListViews(ListView):
    model = Task
    template_name = 'TaskList.html'
    context_object_name = 'tasks'


class TaskDetailViews(DetailView):
    model = Task
    template_name = 'TaskDetail.html'
    context_object_name = 'task_info'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'TaskCreate.html'
    form_class = TaskForm
    success_url = reverse_lazy('TaskList')
    
    def form_valid(self,form):
        form.instance.creator = self.request.user
        
        return super().form_valid(form)


        


class EditTaskView(LoginRequiredMixin,UserIsOwnerMixin,UpdateView):
    model = Task
    template_name = 'TaskEdit.html'
    form_class = TaskForm
    success_url = reverse_lazy('TaskList')
    


class DeleteTaskView(LoginRequiredMixin,UserIsOwnerMixin,DeleteView):
    model = Task
    template_name = 'TaskDelete.html'
    success_url = reverse_lazy('TaskList')


