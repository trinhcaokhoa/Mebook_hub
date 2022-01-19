from django.db import models
from rest_framework import fields, serializers
from .models import Book
from django.contrib.auth import get_user_model

class BookSerializer(serializers.Serializer):
    
    class Meta:
        model = Book
        fields = ('id', 'name', 'author', 'area', 'link_to_book')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)
