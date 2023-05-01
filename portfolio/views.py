from django.shortcuts import render
from .models import Project


def home(request):
    all_projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {
        'author': 'Rilson Almeida',
        'projects': all_projects,
        })