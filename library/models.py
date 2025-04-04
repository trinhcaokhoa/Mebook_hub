import os
from django.db import models
from django.urls import reverse
from mebook_project import settings
from users.models import CustomUser
import datetime




class LibraryBook(models.Model):
    owner = models.ForeignKey(  # Owner is set as the current user (By defined function in admin.py)
        CustomUser,
        on_delete=models.CASCADE,
        editable=True, # Set editable = True so that the form.py can work with owner
        null=False,
    )

    title = models.CharField(max_length=200, default='title')
    author = models.CharField(max_length=50, default='author')
    cover = models.FileField(upload_to='covers/', null=True)
    file = models.FileField(upload_to='doc/', null=True)
    description = models.CharField(max_length=1500, default="Not given", null=True)
    date = models.DateTimeField(auto_now_add=True)

    """def __str__(self):        
        return self.date.strftime('%m/%d/%Y')"""

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])



