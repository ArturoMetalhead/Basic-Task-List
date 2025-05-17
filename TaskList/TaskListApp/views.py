from django.shortcuts import render,redirect,get_object_or_404
from .models import Task

def home(request):

    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'TaskListApp/home.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        title = request.POST.get('title', '').strip()

        if task_id:
            task = get_object_or_404(Task, id=task_id)

            if title == '':
                # Si está vacío, eliminar
                task.delete()
            else:
                # Si tiene contenido, actualizar
                task.title = title
                task.save()
        else:
            if title != '':
                Task.objects.create(title=title)

    return redirect('home')


def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
    return redirect('home')