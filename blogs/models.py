from django.db import models


# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    content = models.TextField()
    img_url = models.CharField(max_length=3083)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

