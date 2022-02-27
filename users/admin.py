from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import MyBook, CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

CustomUser = get_user_model()

# Book Admin 
class BookAdmin(admin.ModelAdmin):
    list_display = ("id","owner","title", "author", "cover", "file")

    # return the current user as owner
    def save_model(self, request, obj, form, change):
        if obj.id == None:
           obj.owner = request.user
           super().save_model(request, obj, form, change)
        else:
           super().save_model(request, obj, form, change)
admin.site.register(MyBook, BookAdmin)

# User Admin
class CustomAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    models = CustomUser
    list_display = ['id','email', 'username']



admin.site.register(CustomUser, CustomAdmin)



    
