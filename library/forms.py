from django import forms
from .models import LibraryBook
from django.contrib.auth import get_user_model


class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(BookForm, self).__init__(*args, **kwargs)
       self.fields['owner'].widget = forms.widgets.HiddenInput()
    

    class Meta:
        model = LibraryBook     
        fields = ('owner','title', 'author', 'cover', 'file','description')
    

        
