from django.db import models
from django.utils import timezone
from django.urls import reverse

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    started = models.DateField(default=timezone.now())
    ended = models.DateField(default=timezone.now())
    source = models.URLField(max_length=200)
    description = models.CharField(max_length=1000)
    image = models.ImageField(blank=True)
    
    def __str__(self):
        return self.project_name
    
    def get_url(self):
        return reverse("product_detail", kwargs={"id": self.id})

class ProjectImages(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.project.project_name

