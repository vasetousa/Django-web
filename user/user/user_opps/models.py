from django.db import models


# Create your models here.
class SpaceCraft(models.Model):
    craft_name = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.craft_name
