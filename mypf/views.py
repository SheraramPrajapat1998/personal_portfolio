from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Project
from .forms import ContactForm

def home_view(request):
    projects = Project.objects.filter(status='Published')
    return render(request, 'mypf/index.html', { 'projects':projects })

def detail_view(request, year, month, day, project):
    project = get_object_or_404(Project, slug=project, status='Published', publish__year=year, publish__month=month, publish__day=day)
    images = project.other_images.all() # returns queryset of other images
    return render(request, 'mypf/detail.html', {'project':project, 'images':images})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your feedback has been sent. Thanks')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'mypf/contact.html', {'form':form})
    