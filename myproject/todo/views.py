from django.shortcuts import render, redirect
from .models import Todo
from .forms import newTodoForm
from django.views.decorators.http import require_POST


# Create your views here.

def index(request):
    todo_list = Todo.objects.order_by('id')
    todoForm = newTodoForm
    context = {'todo_list': todo_list, 'todoForm': newTodoForm}
    return render(request, 'todo/todoPage.html', context)


@require_POST
def addTodo(request):
    todoform = newTodoForm(request.POST)

    if todoform.is_valid():
        new_todo = todoform.save()

    return redirect('index')


def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')


def deleteComplete(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')


def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')
