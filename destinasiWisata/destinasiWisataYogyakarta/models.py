from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image_url = models.URLField()
    address = models.TextField()
    site = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# class User(models.Model):
#     username = models.CharField(max_length=50)
#     email = models.EmailField()
#     password = models.CharField(max_length=50)

#     def __str__(self):
#         return self.username