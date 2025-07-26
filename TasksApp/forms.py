from django import forms
from TasksApp.models import Task

class TaskForm(forms.ModelForm):
    class Meta():
        model = Task
        fields = ['title','description','status','priority','deadline'] 
