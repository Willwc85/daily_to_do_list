from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm
from .models import Task


# Create your views here.
def taskList(request):
    tasks = Task.objects.all().order_by('title')
    return render(request, 'tasks/list.html', {'tasks': tasks})


def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})

def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)  # Corrigido: Criar a instância do formulário com dados POST
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')
    else:
        form = TaskForm()  # Corrigido: Usar TaskForm com inicial maiúscula
    return render(request, 'tasks/addtask.html', {'form': form})

def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)

        if(form.is_valid()):
            task.save()
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

def helloworld(request):
    return HttpResponse('Hello World')

def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})
