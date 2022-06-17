from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from online_music.validators.validators import only_letters_numbers_underscore_validator, negative_number_validator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(2),
                    only_letters_numbers_underscore_validator],  # could use regex to validate
    )

    email = models.EmailField()

    age = models.IntegerField(
        blank=True,
        null=True,
        validators=[negative_number_validator],
    )


class Album(models.Model):
    MUSIC_CHOICES = [(w, w) for w in (
        'Pop Music', 'Jazz Music', 'R&B Music', 'Rock Music', 'Country Music', 'Dance Music', 'Hip Hop Music',
        'Other')]

    album_name = models.CharField(
        max_length=30,
        unique=True,
    )

    artist = models.CharField(
        max_length=30,
    )

    genre = models.CharField(
        max_length=30,
        choices=MUSIC_CHOICES
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=[negative_number_validator]
    )

    @property
    def truncated_price(self):
        return f'{self.price:.2f}'
