from django.contrib.auth import models as auth_models
from django.db import models

# Create your models here.
from petstagram.accounts.managers import PetstagramUserManager

'''
1. Create model extending .....
2. Configure this model in settings.py
3. Create user manager for the model to use
'''


class PetstagramUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LEN = 25

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = PetstagramUserManager()