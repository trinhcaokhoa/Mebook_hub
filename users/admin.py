from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import  CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

CustomUser = get_user_model()


# User Admin
class CustomAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    models = CustomUser
    list_display = ['id','email', 'username']



admin.site.register(CustomUser, CustomAdmin)



    
