from asyncio.format_helpers import _format_callback
from re import template
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

class SignUpPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    sucess_url = reverse_lazy('login')
    template_name = 'signup.html'
