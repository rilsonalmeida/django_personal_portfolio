from django.contrib import admin

from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = 'id', 'title',
    list_display_links = 'id', 'title',
    list_per_page = 12
    search_fields = 'id', 'title', 'description'
    ordering = ('-id', )