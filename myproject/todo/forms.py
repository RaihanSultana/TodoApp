from django import forms
from .models import Todo

# class TodoForm(forms.Form):
#     task=forms.CharField(max_length=255, widget = forms.TextInput(attrs={'placeholder': 'Enter task name'}))

class newTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text']
        widgets= {'text': forms.TextInput(attrs={'placeholder': 'Enter task name'})}
