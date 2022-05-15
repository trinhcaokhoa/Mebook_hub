from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import LibraryView, BookListView, BookDetailView, SearchView, upload_file

urlpatterns = [
    path('', LibraryView.as_view(), name='library'),
    path('mybooks/', BookListView.as_view(), name='mybooks'),
    path('<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('search/',SearchView.as_view(),name='search_results'),
    path('upload/', upload_file, name='upload_file'),
    #path('download/', BookDetailView.download_file, name='download_file'),
]
