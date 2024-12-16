from django.db import models
from django.utils import timezone  # Ensure to import timezone for current time

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')
    created_at = models.DateTimeField(auto_now_add=True)  # auto_now_add for created_at
    updated_at = models.DateTimeField(auto_now=True)  # auto_now for updated_at
    
    def __str__(self):
        return self.title
