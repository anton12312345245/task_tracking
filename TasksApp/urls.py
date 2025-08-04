from django.urls import path
from TasksApp import views



urlpatterns = [
    path('',views.TaskListViews.as_view(),name='TaskList'),
    path('<int:pk>',views.TaskDetailViews.as_view(),name='TaskDetail'),
    path('TaskCreate',views.TaskCreateView.as_view(),name='TaskCreate'),
    path('<int:pk>/edit',views.EditTaskView.as_view(),name='TaskEdit'),
    path('<int:pk>/delete',views.DeleteTaskView.as_view(),name='TaskDelete'),
    path('<int:pk>/CommentDelete',views.DeleteComment.as_view(),name='CommentDelete'),
    path('<int:pk>/ChangeStatus',views.ChangeStatusView.as_view(),name='ChangeStatus')
]