
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


class SignUpPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    sucess_url = reverse_lazy('login.html')
    template_name = 'signup.html'





