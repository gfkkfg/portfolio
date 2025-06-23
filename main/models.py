from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web'),
        ('android', 'Android'),
        ('ai', 'AI'),
        ('iot', 'IoT'),
        ('others', 'Others'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    project_link = models.URLField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='others')

    def __str__(self):
        return f"{self.title} ({self.category})"


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f"Image for {self.project.title}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
