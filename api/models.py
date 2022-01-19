from django.db import models



class Book(models.Model):
    name = models.CharField(max_length=200, default="")
    author = models.CharField(max_length=20, default="")
    area = models.CharField(max_length=20)
    link_to_book = models.CharField(max_length=200)
