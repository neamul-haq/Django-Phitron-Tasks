from django.shortcuts import render
from . forms import djangoForm
from . models import modelForm
# Create your views here.

def django_form(request):
    form = djangoForm()
    return render(request, 'myapp/form.html',{'form':form})

def model_form(request):
    modelform = modelForm.objects.all()
    return render(request, 'myapp/model_form.html',{'modelform': modelform})