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

    def __init__(self, *args, **kwargs):
        super(TaskFilterForm, self).__init__(*args, **kwargs)
        self.fields["status"].widget.attrs.update({"class": "form-control"})
        self.fields["priority"].widget.attrs.update({"class": "form-control"})



class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['content']
  def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields["content"].widget.attrs.update({"class": "form-control"})



