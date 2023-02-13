
import os
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse 
from django.views.generic import ListView, DetailView
from .models import LibraryBook
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.validators import URLValidator
import urllib.request
import matplotlib.dates
import plotly.graph_objs as go





class LibraryView(ListView): # View all the book
    model = LibraryBook
    context_object_name = 'library'
    template_name = 'library/library.html'


class BookListView(LoginRequiredMixin,ListView):  # View the book of the current user
    model = LibraryBook
    login_url = '/accounts/login/'
    #redirect_field_name = 'redirect_to'
    context_object_name = 'mybooks'
    template_name = 'library/mybooks.html'

    '''def get_queryset(self):
        # original qs
        qs = super().get_queryset()        
        # filter by curent user 
        return qs.filter(owner=self.request.user)'''

    def get_context_data(self):
        context = {}
        # get query
        my_books = super().get_queryset().filter(owner=self.request.user).order_by('date')
        dateslist = list(my_books.values('date'))
        context['mybooks'] = my_books
        # handle data from datetime to number
        x_values = []
        for i in dateslist:
            date = i.get('date')
            x_values.append(date)
        dates = matplotlib.dates.date2num(x_values)
        
        counts = list(range(1,len(dates)+1))
        
        # draw the grap
        post_line = go.Scatter(
                    x=x_values, 
                    y=counts,
                    mode='lines+markers',
                    name="Books Uploaded",    
                              
                    )

        data = [ post_line, ]  

        layout = go.Layout( showlegend=True, 
                            paper_bgcolor='rgb(233,233,233)',
                            plot_bgcolor='rgba(0,0,0,0)',
        )

        fig = go.Figure(data=data, layout=layout)
        chart  = fig.to_html(full_html=False, default_height=500, default_width=700)
        
        context['chart'] = chart
        return context


class BookDetailView(DetailView):  # Get the book detail, download, upload review
    model = LibraryBook
    context_object_name = 'book_detail'
    template_name = 'library/book_detail.html' 

    def get_object(self, queryset=None): # set the instance as the current BookDetailView object by looking at primary key
        BookDetailView.obj = LibraryBook.objects.get(pk=self.kwargs.get("pk"))
        return super().get_object() # Return nothing

    def get_success_url(self):
        return reverse('library', kwargs={'pk': self.object.pk})

    '''def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        #context['review_form'] = self.get_form()
        return context'''
    
    def download_file(request):
        filename = BookDetailView.obj.file
        file_path = os.path.join(
            settings.MEDIA_URL, str(filename))
        print(file_path)
        if URLValidator(file_path):
            with urllib.request.urlopen(file_path) as fh:
                response = HttpResponse(
                    fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'inline; filename=' + \
                    os.path.basename(file_path)
            return response
        else:
            print(os.path.exists(file_path))
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

@login_required
def upload_file(request):  # method to upload a book to library
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if settings.USE_S3:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/library/')

    else:
        form = BookForm({'owner': request.user})
    return render(request, 'library/upload.html', {'form': form})



    
    

