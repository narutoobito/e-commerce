from django.db import models
from django.contrib.auth.models import User
from shop.models import Products
# Create your models here.

class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buyer")
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="bought")

    def __str__(self):
        return f"{self.owner} {self.product}"