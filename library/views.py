from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q 
from django.views.generic import ListView, DetailView
from .models import LibraryBook
from .forms import BookForm
from django.contrib.auth import get_user_model




class LibraryView(ListView): # View all the book
    model = LibraryBook
    context_object_name = 'library'
    template_name = 'library/library.html'


class BookListView(ListView): # View the book of the current user

    model = LibraryBook
    context_object_name = 'mybooks'
    template_name = 'library/mybooks.html'

    def get_queryset(self):
        # original qs
        qs = super().get_queryset()
        # filter by a variable captured from url, for example
        return qs.filter(owner=self.request.user)


class BookDetailView(DetailView): # Get the book detail, download
    model = LibraryBook
    context_object_name = 'book_detail'
    template_name = 'library/book_detail.html'

    

class SearchView(ListView): # Search the book with the q = keyword
    model = LibraryBook
    context_object_name = 'search_results'
    template_name = 'library/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return LibraryBook.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )


def upload_file(request): # method to upload a book to library
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/library/')
    else:        
        form = BookForm({'owner': request.user})
    return render(request, 'library/upload.html', {'form': form})


def dowload_file(request):
    return None



