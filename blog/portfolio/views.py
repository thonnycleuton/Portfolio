from django.shortcuts import render, get_object_or_404
from blog.portfolio.models import Project, Category


def index(request):
    projects = Project.objects.all()
    categories = Category.objects.filter(project__in=projects).distinct()
    template_name = 'portfolio/index.html'
    context = {
        'projects': projects, 'categories': categories,
    }
    return render(request, template_name, context)


def details(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {
        'project': project
    }
    template_name = 'portfolio/details.html'
    return render(request, template_name, context)
