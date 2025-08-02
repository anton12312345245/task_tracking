from django import forms
from TasksApp.models import Task,Comment

class TaskForm(forms.ModelForm):
    class Meta():
        model = Task
        fields = ['title','description','status','priority','deadline'] 

class TaskFilterForm(forms.Form):
        
    priority_choices = [('','All'),('low','Low'),('medium','Medium'),('high','High')]
    status_choices = [('','All'),('todo','To do'),('in_progress','In progress'),('done','Completed')]

    priority = forms.ChoiceField(choices=priority_choices,required=True,label='priority')
    status = forms.ChoiceField(choices=status_choices,required=True,label='status')

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['content']

