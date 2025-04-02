from django import forms
from .models import Category

class NewTaskForm(forms.Form):
    task = forms.CharField(
        label='',  
        widget=forms.TextInput(attrs={
            'autofocus': 'autofocus', 
            'id': 'task', 
            'placeholder': 'New Task'  
        })
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.Select(attrs={'id': 'category'}),
        label="Category"
    )