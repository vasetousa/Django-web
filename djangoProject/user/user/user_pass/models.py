from django.contrib.auth import models as auth_models
from django.db import models

from user.user_pass.managers import AppUsersManager


class UserModel(models.Model):
    first_name = models.CharField(
        max_length=20,
    )

    last_name = models.CharField(
        max_length=20,
    )

    email = models.EmailField()


class Department(models.Model):
    name = models.CharField(
        max_length=30,
    )

    def __str__(self):
        return f'({self.name})'

    class Meta:
        ordering = ('name',)


class Employee(models.Model):
    first_name = models.CharField(
        max_length=20,
    )

    last_name = models.CharField(
        max_length=20,
    )

    employment_date = models.DateField(
        auto_now_add=True,
    )

    termination_date = models.CharField(
        max_length=10,
        default='current',
        null=True,
        blank=True,
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'  # {self.employment_date} {self.termination_date}'


class Manager(models.Model):
    first_name = models.CharField(
        max_length=20,
    )

    last_name = models.CharField(
        max_length=20,
    )

    employees = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
    )

    assigned_to_team = models.DateTimeField(
        auto_now_add=True,
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'({self.first_name} {self.last_name})'


'''
1. Create a model extending AbstractBaseUser and PermissionsMixin
2. Tell Django about your new user model (settings -> AUTH_USER_MODEL = 'appname.modelname')
3. Create user manager for the administration to work
4. 'objects' now will come from our manager class
'''


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    is_staff = models.BooleanField(
        default=False,
    )
    ''' 'date_joined' was taken from the db '''
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    objects = AppUsersManager()

    USERNAME_FIELD = 'email'
