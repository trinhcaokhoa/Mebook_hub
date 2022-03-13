
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import LibraryBook



class LibraryView(ListView):
    model = LibraryBook
    context_object_name = 'library'
    template_name = 'library/library.html'


class BookListView(ListView):

    model = LibraryBook
    context_object_name = 'mybooks'
    template_name = 'library/mybooks.html'

    def get_queryset(self):
        # original qs
        qs = super().get_queryset()
        # filter by a variable captured from url, for example
        return qs.filter(owner=self.request.user)


class BookDetailView(DetailView):
    model = LibraryBook
    context_object_name = 'book_detail'
    template_name = 'library/book_detail.html'

