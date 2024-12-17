from django.db import models
from cloudinary.models import CloudinaryField

class Post(models.Model):
    title = models.CharField(max_length=100)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=[('draft', 'Draft'), ('published', 'Published')],
        default='draft'
    )

    def __str__(self):
        return self.title
