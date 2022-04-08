from django.urls import path

from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('all/', views.allTasksView, name='alltasks'),
    path('add/', views.addTaskView, name='addtask'),
    path('update/<str:pk>/', views.updateTaskView, name='updatetask'),
    path('delete/<str:pk>/', views.deleteTaskView, name='deletetask'),
    path('done/<str:pk>/', views.doneTaskView, name='donetask')
]