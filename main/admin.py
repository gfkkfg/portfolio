from django.contrib import admin
from .models import Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1 

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ('title', 'tech_stack', 'project_link')
    fields = ('title', 'description', 'tech_stack', 'project_link') 

admin.site.register(Project, ProjectAdmin)
