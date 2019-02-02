from django.shortcuts import render, redirect
from .models import List, Task
from .forms import SearchForm, ListForm


def show_lists(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            search = form.cleaned_data['name']
            context = {
                'lists': List.objects.filter(name__contains=search),
                'form': form
            }
            return render(request, 'todo/lists.html', context)
        if request.GET.get('order', '') != '':
            context = {
                'lists': List.objects.order_by('name')
            }
            return render(request, 'todo/lists.html', context)
    context = {
        'lists': List.objects.all(),
    }
    return render(request, 'todo/lists.html', context)


def todo_list(request, list):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            search = form.cleaned_data['name']
            tasks = Task.objects.filter(mark = False, list_id = list)
            context = {
                'tasks': tasks.filter(name__contains = search),
                'form': form
            }
            return render(request, './todo/todo_list.html', context)
    if request.GET.get('order', '') != '':
        tasks = Task.objects.filter(mark = False, list_id=list)
        context = {
            'tasks': tasks.order_by(request.GET.get('order', ''))
        }
        return render(request, 'todo/todo_list.html', context)
    if request.POST.get('done_id', '') != '':
        task = Task.objects.get(id = 'done_id')
        task.mark = True
        task.save()
        return redirect('../todo_list')
    tasks = Task.objects.filter(mark = False, list_id = list)
    context = {
        'tasks': tasks
    }

    return render(request, 'todo/todo_list.html', context)


def completed_todo_list(request, list):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            search = form.cleaned_data['name']
            tasks = Task.objects.filter(mark = True, list_id = list)
            context = {
                'tasks': tasks.filter(name__contains = search),
                'form': form
            }
            return render(request, 'todo/completed_todo_list.html', context)
    if request.GET.get('order', '') != '':
        tasks = Task.objects.filter(mark = True, list_id = list)
        context = {
            'tasks': tasks.order_by('name'),
        }
        return render(request, 'todo/completed_todo_list.html', context)
    tasks = Task.objects.filter(mark = True, list_id = list)
    context = {
        'tasks': tasks,
    }
    return render(request, 'todo/completed_todo_list.html', context)


def create_list(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('./')
    else:
        form = ListForm()
    context = {
        'form': form
    }
    return render(request, 'todo/create_list.html', context)


def make_done(request, fk, pk):
    task = Task.objects.get(pk=pk)
    task.mark = True
    task.save()
    return redirect('../todo')


def make_notdone(request, fk, pk):
    task = Task.objects.get(pk=pk)
    task.mark = False
    task.save()
    return redirect('../completed')


def delete_list(request, fk):
    del_list = List.objects.get(pk=fk)
    del_list.delete()
    return redirect('..')