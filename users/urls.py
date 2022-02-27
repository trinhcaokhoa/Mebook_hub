from django.urls import path
from .views import SignUpPageView, BookListView, BookDetailView

urlpatterns =[
    path('signup/', SignUpPageView.as_view(), name='signup'),
    path('mybooks/', BookListView.as_view(), name='books_list'),
    path('<int:pk>', BookDetailView.as_view(), name='book_detail'),
]