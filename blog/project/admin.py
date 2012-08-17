from project.models import Project
from django.contrib import admin




class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'url')

admin.site.register(Project, ProjectAdmin)
