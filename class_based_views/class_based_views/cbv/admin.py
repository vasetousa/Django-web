from django.contrib import admin

# Register your models here.
from class_based_views.cbv.models import Category, Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
