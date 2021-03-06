from django.db import models

class Product(models.Model):
    title       = models.CharField(max_length=100) 
    description = models.TextField(blank=False)
    price       = models.DecimalField(decimal_places=2, max_digits=10)
    agree       = models.BooleanField(default=False)
    feature     = models.BooleanField(default=False)
