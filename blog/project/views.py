from project.models import Project
from django.shortcuts import render, render_to_response, get_object_or_404
# Create your views here.

def index(request):
    projects = Project.objects.all()
    return render_to_response("projects/index.html", {'projects' : projects})

def detail(request, project_id):
    p = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/detail.html', {'project' : p})
