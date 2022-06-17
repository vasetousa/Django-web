import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from cbv_petstagram.petstagram.validators import only_letters_validator

# Create your models here.
UserModel = get_user_model()


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    # id/pk by default
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_letters_validator,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            only_letters_validator,
        )
    )

    picture = models.URLField(
        null=True,
        blank=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )
    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        default=DO_NOT_SHOW,

        # if is verification is needed:
        # if value == 'Male' =>> Bad, cuz hardcoded
        # if value == Profile.MALE =>> Good
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Pet(models.Model):
    # constants

    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'

    NAME_MAX_LENGTH = 30
    TYPES = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]

    # fields(columns)
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
    )
    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )
    pet_date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    @property
    def age(self):
        return datetime.datetime.now().year - self.pet_date_of_birth.year

    # one-to-one relations (if any)

    # one-to-many relations (if any)
    user_profile = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name} ({self.type})'

    # many-to-many relations (if any)

    owner = models.CharField(
        max_length=23,
    )

    # properties
    # methods
    # dunder methods
    # meta
    class Meta:
        # unique_together = ('user_profile', 'name')
        pass





class PetPhoto(models.Model):
    pet_picture = models.ImageField(
        validators=(
            # image_size_validator(5),
        )
    )
    tagged_pets = models.ManyToManyField(
        Pet,
        # validate at least one pet next lesson
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    publication_date = models.DateTimeField(
        auto_now_add=True,
    )
    likes = models.IntegerField(
        default=0,
    )
