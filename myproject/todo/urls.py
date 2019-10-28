from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deleteComplete', views.deleteComplete, name='delete1'),
    path('deleteAll', views.deleteAll, name='delete2')
]
