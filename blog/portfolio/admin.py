from django.contrib import admin
from .models import Project, Category, Client, ProjectImage

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Client)
admin.site.register(ProjectImage)
