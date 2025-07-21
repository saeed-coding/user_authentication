from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)


class Accounts(models.Model):
    # id = models.AutoField()
    name = models.CharField()
    user_name = models.CharField(max_length=25)
    password = models.CharField(max_length=40)

class Cars(models.Model):
    name = models.CharField()
    speed = models.IntegerField()

    def __str__(self):
        return self.name




