from django.contrib import admin

# Register your models here.
from Bootcamp.products.models import Product


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    pass

