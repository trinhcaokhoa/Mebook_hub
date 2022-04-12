import os
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.db.models import Q 
from django.views.generic import ListView, DetailView
from .models import LibraryBook
from .forms import BookForm


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

    def get_object(self, queryset=None): # set the instance as the current BookDetailView object by looking at primary key
        BookDetailView.obj = LibraryBook.objects.get(pk=self.kwargs.get("pk"))
        return super().get_object() # Return nothing
    
    def download_file(request):
        filename = BookDetailView.obj.file
        file_path = os.path.join(
            settings.MEDIA_ROOT, str(filename))
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(
                fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'inline; filename=' + \
                    os.path.basename(file_path)
            return response
        raise Http404
        
    

class SearchView(ListView): # Search the book with the q = keyword
    model = LibraryBook
    context_object_name = 'search_results'
    template_name = 'library/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return LibraryBook.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )


def upload_file(request):  # method to upload a book to library
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/library/')        
    else:
        form = BookForm({'owner': request.user})
    return render(request, 'library/upload.html', {'form': form})









