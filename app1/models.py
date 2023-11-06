from django.db import models

# Create your models here.

class product_detail(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.PositiveIntegerField()
    offer = models.BooleanField()
    