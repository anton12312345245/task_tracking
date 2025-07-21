from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    priority_choices = [('low','Low'),('medium','Medium'),('high','High')]
    status_choices = [('todo','To do'),('in_progress','In progress'),('done','Completed')]
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50,choices=status_choices)
    priority = models.CharField(max_length=50,choices=priority_choices)
    deadline = models.DateField(null=True,blank=True) 
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title