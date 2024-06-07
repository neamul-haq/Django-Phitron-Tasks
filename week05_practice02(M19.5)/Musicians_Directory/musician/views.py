from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from . import forms
from . import models
# Create your views here.

@method_decorator(login_required, name='dispatch')
class AddMusicianCreateView(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')
    def form_valid(self, form):
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class EditMusicianView(UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')



@method_decorator(login_required, name='dispatch')
class DeleteMusicianView(DeleteView):
    model = models.Musician
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'


