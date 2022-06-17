from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from expensesTracker.web.constants import constants as con
from expensesTracker.web.validators import validate_only_letters, MaxFileSizeInMbValidator


# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(
        max_length=con.FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(con.FIRST_NAME_MIN_LEN),
            validate_only_letters,
        )
    )
    last_name = models.CharField(
        max_length=con.LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(con.LAST_NAME_MIN_LEN),
            validate_only_letters,
        )
    )
    budget = models.FloatField(
        default=con.BUDGET_DEFAULT_VALUE,
        validators=(
            MinValueValidator(con.BUDGET_MIN_VALUE),
        )
    )
    profile_image = models.ImageField(
        upload_to=con.IMAGE_UPLOAD_TO_DIR,
        # default='/staticfiles/images/user.png',   optional, too many users, too many --
        #                       -- saves in db. Better do it in the html
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(con.IMAGE_MAX_SIZE_IN_MB),
        )
    )
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Expense(models.Model):
    title = models.CharField(
        max_length=con.TITLE_MAX_LEN,
    )

    image = models.URLField()

    price = models.FloatField()

    description = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('title', 'price')



