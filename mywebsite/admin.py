from django.contrib import admin

from .models import Project, ProjectImages

class ProjectImageAdmin(admin.StackedInline):
    model = ProjectImages

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageAdmin]

    class Meta:
       model = Project

@admin.register(ProjectImages)
class ProjectImageAdmin(admin.ModelAdmin):
    pass
