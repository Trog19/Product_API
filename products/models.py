from django.db import models
from django.forms import CharField

# Create your models here.


class Products(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory_quantity = models.IntegerField()
    picture = models.CharField(max_length=5000)