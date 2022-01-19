from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .serializers import BookSerializer, UserSerializer
from .models import Book

# Create your views here.
class BookView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UserViewSet(viewsets.ModelViewSet):  # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
