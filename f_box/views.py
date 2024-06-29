from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')  # Redirect to the todo_list page after saving
    else:
        form = TodoForm()
    return render(request, 'f_box/add_todo.html', {'form': form})

def todo_list(request):
    todos = Todo.objects.all()  # Fetch all todos from the database
    return render(request, 'f_box/todo_list.html', {'todos': todos})
