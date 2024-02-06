from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser, Permission
from django.conf import settings


class Users(AbstractUser):
    """Declare a model for users named 'Users' to store them in the database."""

    groups = models.ManyToManyField('auth.Group', related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions_set')
    # Exclude built-in fields of the standard django model.
    email = None  # models.EmailField(unique=True, blank=True, null=True)
    last_name = None  # models.CharField(max_length=20, blank=True, null=True)
    first_name = None  # models.CharField(max_length=20, blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # Renames the instances of the model with their username.
    def __str__(self):
        return self.username


class User(models.Model):
    """Declare a user data model named "User" to store this data in the database."""

    location = models.CharField(max_length=255, null=False, default='somewhere')
    date = models.DateField()
    forecast = models.CharField(max_length=50, null=False, default='sun')
# With the CASCADE option, deleting a user from the table in
# the database for a model named Users removes all rows
# related with that user from the table in the database for a model named Users.
    user_from_users = models.ForeignKey(Users, on_delete=models.CASCADE)

    def setter_date(self):
        return date.today()

    # Can set the date by through the __init__ statement instead
   # def _init__(self, *args, **kwargs):
       # super(User, self).__init__(*args, **kwargs)
       # self.date = date.today()

# Renames the instances of the model with their username
# obtain by id from related the model instance named 'Users'.
    def __str__(self):
        return self.user_from_users.username
