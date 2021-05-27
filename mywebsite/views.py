from django.shortcuts import render, get_object_or_404

from .models import Project, ProjectImages


def home(request):
    project = Project.objects.all()
    context = {
        'projects': project
    }
    return render(request, 'mywebsite/home.html', context)

def projectview(request, id):
    project = get_object_or_404(Project, id=id)
    photos = ProjectImages.objects.filter(project = project)
    context = {
        'project' : project,
        'photos' : photos
    }
    return render(request, 'mywebsite/projectview.html', context)