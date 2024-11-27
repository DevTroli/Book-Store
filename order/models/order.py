from django.contrib.auth.models import User
from django.db import models

from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)

    class Meta:
        app_label = "order"  # Adicione esta linha

    def __str__(self):
        return f"Order by {self.user.username}"
