from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=20)
    basic=models.IntegerField(default=10000)