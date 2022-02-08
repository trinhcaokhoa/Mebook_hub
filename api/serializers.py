from django.db import models
from rest_framework import fields, serializers
from .models import Book
from django.contrib.auth import get_user_model

class BookSerializer(serializers.Serializer):
    
    class Meta:
        model = Book
        fields = ('id', 'name', 'author', 'area', 'link_to_book')


<<<<<<< HEAD
class UserSerializer(serializers.ModelSerializer):   
=======
class UserSerializer(serializers.ModelSerializer):
>>>>>>> ce2eab8c22d7b4d9a50e15c0957c2041288428c8

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)
