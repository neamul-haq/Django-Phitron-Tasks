from django import forms
from .models import Tasks

class TasksForm(forms.ModelForm):
    taskDescription = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4})
    )
    class Meta: 
        model = Tasks
        fields = '__all__'
