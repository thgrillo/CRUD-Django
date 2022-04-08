from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Task
from .forms import CreateTaskForm

# Create your views here.
def homeView(request):
    tasks = Task.objects.all()
    if request.method == 'GET':
        form = CreateTaskForm()
    else:
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form, 'tasks': tasks}
    return render(request, 'task/home.html', context)

def doneTaskView(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.done = True
        task.save()
        return redirect('/')
    context = {'task': task}
    return render(request, 'task/donetask.html', context)

def allTasksView(request):
    tasks = Task.objects.all()
    return render(request, 'task/alltasks.html', {'tasks': tasks})

def addTaskView(request):
    if request.method == 'GET':
        form = CreateTaskForm()
    else:
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/all/')
    context = {'form': form}
    return render(request, 'task/addtask.html', context)

def updateTaskView(request, pk):
    task = Task.objects.get(id=pk)
    form = CreateTaskForm(instance=task)
    if request.method == 'POST':
        form = CreateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'task': task, 'form': form}
    return render(request, 'task/updatetask.html', context)

def deleteTaskView(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item': item}
    return render(request, 'task/deletetask.html', context)
