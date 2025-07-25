from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Receipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='images')


