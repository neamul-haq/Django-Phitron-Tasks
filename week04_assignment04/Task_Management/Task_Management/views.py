from django.shortcuts import render
from tasks.models import Tasks

def show_tasks(request):
    data = Tasks.objects.all()
    return render(request, 'show_tasks.html', {'data' : data})