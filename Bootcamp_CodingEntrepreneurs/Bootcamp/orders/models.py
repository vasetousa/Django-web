from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from Bootcamp.products.models import Product

User = get_user_model()

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('stale', 'Stale'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)


class Order(models.Model):
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
    )

    product = models.ForeignKey(
        Product,
        null=True,
        on_delete=models.SET_NULL,
    )  # on_delete, record of the order will stay in the db

    status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS_CHOICES,
        default='created',
    )

    subtotal = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )  # 9.99

    tax = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )  # 9.99

    total = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )  # 9.99

    paid_value = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )  # 9.99

    shipping_address = models.TextField(
        blank=True,
        null=True,
    )

    billing_address = models.TextField(
        blank=True,
        null=True,
    )

    timestamp = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.product},     ({self.status})'