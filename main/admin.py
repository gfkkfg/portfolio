from django.contrib import admin
from .models import Project, ProjectImage
from django.utils.html import format_html

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ('title', 'tech_stack', 'github_link')
    fields = ('title', 'description', 'tech_stack', 'github_link')

    def github_link(self, obj):
        if obj.github_link:
            return format_html(f'<a href="{obj.github_link}" target="_blank">GitHub Repo</a>')
        return "-"
    github_link.short_description = "GitHub Link"

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

admin.site.register(Project, ProjectAdmin)
