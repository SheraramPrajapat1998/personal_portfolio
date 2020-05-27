from django.shortcuts import render, redirect, get_object_or_404

from .models import Project

def home_view(request):
    projects = Project.objects.filter(status='Published')
    return render(request, 'mypf/index.html', { 'projects':projects })
