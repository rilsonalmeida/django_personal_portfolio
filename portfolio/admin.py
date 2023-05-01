from django.contrib import admin

from .models import Project

@admin.register(Project)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = 'id', 'title',
    list_display_links = 'id', 'title',
    list_per_page = 12
    search_fields = 'id', 'title', 'description'
    ordering = ('-id', )