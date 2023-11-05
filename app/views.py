from typing import Any
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy # redirect to some URL
from django.views.generic import CreateView, ListView 
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from app.models import People

class SignUp(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class PeopleForm(ModelForm):
    class Meta:
        model = People
        fields = ['name']

class CreateAnimal(PermissionRequiredMixin,CreateView):
    model = People
    permission_required = ('add_people')
    form_class = PeopleForm
    template_name = 'createpeople.html'
    success_url = reverse_lazy('dashboard')

class Login(LoginView):
    template_name = 'login.html'
    next_page = 'dashboard'

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('dashboard'))
        else:
            return super().get(request, *args, **kwargs)

class Logout(LogoutView):
    next_page = 'dashboard'

class Dashboard(ListView):
    model = User
    template_name = 'dashboard.html'
    context_object_name = 'users'