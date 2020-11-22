from django.db import models

# Create your models here.
class product(models.Model):
    city=models.CharField(max_length=100)
    objects=models.Manager()