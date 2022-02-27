from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from .models import MyBook

class SignUpPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    sucess_url = reverse_lazy('login.html')
    template_name = 'signup.html'


class BookListView(ListView):
    model = MyBook
    context_object_name = 'books_list'
    template_name = 'mybooks/books_list.html'


class BookDetailView(DetailView):
    model = MyBook
    context_object_name = 'book_detail' 
    template_name = 'mybooks/book_detail.html'


