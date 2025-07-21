from django.urls import path
from TasksApp import views



urlpatterns = [
    path('',views.TaskListViews.as_view(),name='tasklist'),
    path('<int:pk>',views.TaskDetailViews.as_view(),name='taskdetail')
]