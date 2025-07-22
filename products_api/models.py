from django.db import models

# Create your models here.


class Products(models.Model):
    title = models.CharField(max_length=150, primary_key=True)
    description = models.TextField()
    price = models.IntegerField()
    size = models.FloatField()

    def __str__(self):
        return self.title


