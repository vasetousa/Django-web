from django.db import models
from django.conf import settings

# Create your models here.
from Bootcamp.accounts.forms import User


class Product(models.Model):
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        # on_delete=models.CASCADE,
    )

    title = models.CharField(
        max_length=20,
    )

    content = models.TextField(
        null=True,
        blank=True,
    )

    price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )  # 9.99

    inventory = models.IntegerField(
        default=0,
    )

    featured = models.BooleanField(
        default=False,
    )

    def has_inventory(self):
        return self.inventory > 0  # True or False

    def __str__(self):
        return self.title
