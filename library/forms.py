from django import forms
from django.forms import HiddenInput
from .models import LibraryBook
from django.contrib.auth import get_user_model


class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(BookForm, self).__init__(*args, **kwargs)
       self.fields['owner'].widget.attrs['disabled'] = True
    class Meta:
        model = LibraryBook     
        fields = ('owner','title', 'author', 'cover', 'file')
    

        
