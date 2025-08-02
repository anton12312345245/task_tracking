from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from TasksApp.models import Task,Comment
from django.urls import reverse_lazy
from TasksApp.forms import TaskForm
from django.contrib.auth.mixins import  LoginRequiredMixin
from TasksApp.mixins import UserIsOwnerMixin
from TasksApp.forms import TaskFilterForm,CommentForm

class TaskListViews(ListView):
    model = Task
    template_name = 'TaskList.html'
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskFilterForm(self.request.GET)

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get('status','')
        priority = self.request.GET.get('priority','')
        if status:
            queryset = queryset.filter(status=status)
        if priority:
            queryset = queryset.filter(priority=priority)
        return queryset

    
class TaskDetailViews(DetailView):
    model = Task
    template_name = 'TaskDetail.html'
    context_object_name = 'task_info'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context 
    
    def post(self,request,*args,**kwargs):
        Comment_Form = CommentForm(request.POST)
        if Comment_Form.is_valid():
            comment = Comment_Form.save(commit=False)
            comment.creator =  request.user
            comment.task = self.get_object()
            comment.save()
            return redirect('TaskDetail',pk=comment.task.pk)


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


class DeleteComment(LoginRequiredMixin,UserIsOwnerMixin,DeleteView):
    model = Comment
    template_name = 'CommentDelete.html'
    def get_success_url(self):
        return reverse_lazy('TaskDetail',kwargs={'pk':self.object.task.pk}) 

    