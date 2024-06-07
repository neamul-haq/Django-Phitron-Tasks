from django.shortcuts import redirect
from . import forms
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
# Create your views here.

class registerView(CreateView):
    model = User
    form_class = forms.RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('user_login')
    def form_valid(self, form):
        return super().form_valid(form)



class UserLoginView(LoginView):
    template_name = 'register.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('homepage')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context


class UserLogoutView(LogoutView):
    def get(self, request):
        logout(request)
        return redirect('user_login')

def user_logout(request):
    logout(request)
    return redirect('homepage')
