from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image_url = models.URLField()
    address = models.TextField()
    site = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name