from django.contrib import admin
from .models import Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1 

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

admin.site.register(Project, ProjectAdmin)
