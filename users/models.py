
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# User model
class CustomUser(AbstractUser):
    pass
    


# Book of user model
class MyBook(models.Model):
    owner = models.ForeignKey(  #Owner is set as the current user (By defined function in admin.py)
        CustomUser,
        on_delete=models.SET_NULL,
        editable=False,
        null=True
    )       
    
    title = models.CharField(max_length=200, default='title')
    author = models.CharField(max_length=50, default='author')
    cover = models.ImageField(upload_to='covers/', null=True)
    file = models.FileField(upload_to='doc/', null=True)
     

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])

    



















