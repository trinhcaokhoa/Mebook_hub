from unicodedata import name
from urllib.parse import urlparse
from django.urls import path
from .views import SignUpPageView

urlpatterns =[
    path('signup/', SignUpPageView.as_view(), name='signup')
]