from django.urls import path
from .views import BookView

urlpatterns = [
    path('book_api', BookView.as_view()),
]