from django.shortcuts import redirect, get_object_or_404, render
from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task = task)
    return redirect('home')

def mark_as_done(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')


def delete_task(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')

def edit_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        task.task = request.POST['task']
        task.save()
        return redirect('home')
        
    return render(request,'home.html',{
        'edit_task':task,
        'not_completed_tasks': Task.objects.filter(is_completed=False).order_by('-updated_at'),
        'completed_tasks': Task.objects.filter(is_completed=True).order_by('-updated_at'),
    })