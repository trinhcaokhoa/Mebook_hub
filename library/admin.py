from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import LibraryBook

# Book Admin


class LibraryAdmin(admin.ModelAdmin):
    readonly_fields = ['id','owner']
    list_display = ("id", "owner", "title", "author", "cover", "file","description","date")
   
    # return the current user as owner in admin page
    def save_model(self, request, obj, form, change):
        if obj.id == None:
           obj.owner = request.user
           super().save_model(request, obj, form, change)
        else:
           super().save_model(request, obj, form, change)


admin.site.register(LibraryBook,LibraryAdmin)


