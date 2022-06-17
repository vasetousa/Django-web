from django.contrib import admin

# Register your models here.
from user.user_opps.models import SpaceCraft


@admin.register(SpaceCraft)
class SpaceCraftAdmin(admin.ModelAdmin):
    pass
