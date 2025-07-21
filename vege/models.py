from django.db import models

# Create your models here.


class Receipe(models.Model):
    name = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='images')


