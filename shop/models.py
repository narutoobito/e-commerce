from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=64)
    product_type = models.CharField(max_length=64)
    price = models.CharField(max_length=10, default="0 Rupees")
    description = models.TextField()
    product_image = models.ImageField(upload_to='images/')


    def __str__(self):
        return f"{self.name} {self.product_type} {self.price}"
