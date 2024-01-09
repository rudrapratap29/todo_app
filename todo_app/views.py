from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings


def user_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'],
            password = form.cleaned_data['password'],
            Email = form.cleaned_data['email'])
            
            if user is not None:
                login(request,user)
                return redirect('task_list')
            
            else:
                "invalid credetentials"

    return render(request,'todo/login.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)

            return redirect(settings.LOGIN_REDIRECT_URL)
        
    return render(request,'todo/signup.html',{'form':form})

@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})



@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/task_form.html', {'form': form})



@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todo/task_detail.html', {'task': task})



@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/task_form.html', {'form': form})



@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todo/task_confirm_delete.html', {'task': task})


@login_required
def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = True
    task.save()
    return redirect('task_list')
