import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.main.validators import only_letters_validator, image_size_validator

'''
The user must provide the following information in their profile:
The first name - it should have at least 2 chars, max - 30 chars, and should consist only of letters.
The last name - it should have at least 2 chars, max - 30 chars, and should consist only of letters.
Profile picture - the user can link their picture using a URL.

The user may provide the following information in their profile:
Date of birth: day, month, and year of birth.
Description - a user can write any description about themselves, no limit of words/chars.
Email - a user can only write a valid email address.
Gender - the user can choose one of the following: "Male", "Female", and "Do not show".'''

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


'''
The user must provide the following information when adding a pet in their profile:
Name - it should consist of maximum 30 characters. All pets' names should be unique for that user.
Type - the user can choose one of the following: "Cat", "Dog", "Bunny", "Parrot", "Fish", or "Other".
The user may provide the following information when adding a pet to their profile:
Date of birth - pet's day, month, and year of birth.
Pet's Photo
The user must provide the following information when uploading a pet's photo in their profile:
Photo - the maximum size of the photo can be 5MB
Tagged pets - the user should tag at least one of their pets. There is no limit in the number of tagged pets
The user may provide the following information when uploading a pet's photo in their profile:
Description - a user can write any description about the picture, with no limit of words/chars
Other:
Date and time of publication - when a picture is created (only), the date and time of publication are automatically generated.
Likes - each picture has 0 likes at the beginning, and no one can change it. The number of likes a picture can collect is unlimited
'''


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
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name} ({self.type})'

    # many-to-many relations (if any)

    # properties
    # methods
    # dunder methods
    # meta
    class Meta:
        unique_together = ('user', 'name')


class PetPhoto(models.Model):
    pet_picture = models.ImageField(
        # validators=(
        #     image_size_validator(5),
        # )
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

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,

    )