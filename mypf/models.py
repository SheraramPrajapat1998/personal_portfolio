from django.db import models
from django.utils import timezone
from django.urls import reverse


class Project(models.Model):
    STATUS_CHOICES = (
        ('Draft', 'draft'),
        ('Published', 'published'),
    )

    TYPE_CHOICES = (
        ('Back-End', 'Back End'),
        ('Front-End', 'Front End'),
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)
    image = models.ImageField(upload_to='project/') # main image that will be displayed on front  
    descrition = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Draft')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='Back End')

    class Meta:
        ordering = ('-updated', '-publish')

    def __str__(self):
        return self.title
    

class Images(models.Model):
    image = models.ImageField(upload_to='project')
    multi_image = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='other_images')
    