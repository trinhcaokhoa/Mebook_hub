from django.urls import path

from library.views import LibraryView,BookListView,BookDetailView

urlpatterns = [

    path('', LibraryView.as_view(), name='library'),
    path('mybooks/', BookListView.as_view(), name='mybooks'),
    path('<int:pk>', BookDetailView.as_view(), name='book_detail'),
]
