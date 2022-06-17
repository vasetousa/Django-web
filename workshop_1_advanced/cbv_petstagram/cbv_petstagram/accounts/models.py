from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from cbv_petstagram.accounts.managers import PetstagramUserManager

'''
1. Create model extending ...
2. Configer this model in settings.py
3. Create user manager
'''


# creating User data for sign in on the website
class PetstagramUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LEN = 25

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        unique=True,
    )
    # adds date/time when user was created
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    # in permits us to log in admin
    is_staff = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'username'

    objects = PetstagramUserManager()
