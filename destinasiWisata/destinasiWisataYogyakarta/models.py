from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    images = models.URLField()
    address = models.TextField()
    site = models.URLField()
    created_at = models.DateTimeField()        