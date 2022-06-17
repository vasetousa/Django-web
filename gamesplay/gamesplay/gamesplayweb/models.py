from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class Profile(models.Model):
    email = models.EmailField()

    age = models.IntegerField(
        validators=[MinValueValidator(12)],
    )

    password = models.CharField(
        max_length=30
    )

    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'



class Game(models.Model):
    GENRES = [(y, y) for y in ("Action", "Adventure", "Puzzle", "Strategy", "Sports", "Board/Card Game", "Other")]

    title = models.CharField(
        max_length=30,
        unique=True,
    )

    category = models.CharField(
        max_length=15,
        choices=GENRES,
    )

    rating = models.FloatField(
        validators=[MinValueValidator(0.2),
                    MaxValueValidator(5.1)],
    )

    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1)],

    )

    image_url = models.URLField()

    summary = models.TextField(
        null=True,
        blank=True,
    )
