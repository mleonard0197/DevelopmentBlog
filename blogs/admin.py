from django.contrib import admin
from .models import Post


class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at', 'updated_at')


# Register your models here.
admin.site.register(Post, BlogAdmin)