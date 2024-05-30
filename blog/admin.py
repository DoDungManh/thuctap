from django.contrib import admin
from .models import Blog

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title']

admin.site.register(Blog, PostAdmin)

