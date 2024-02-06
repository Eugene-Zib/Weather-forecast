"""This is test task."""

from django import forms
from django.contrib.auth.forms import AuthenticationForm, ReadOnlyPasswordHashField, UserChangeForm, UserCreationForm

from .models import Users


# Creating a form from the standard Django authentication form.
class SignInForm(AuthenticationForm):
    """Authentication form from Django's built-in library."""

    pass


class SignUpForm(UserCreationForm):
    """Creation form for user from Django's built-in library."""

    class Meta:
        # Specify model to be used.
        model = Users
        fields = ['username', 'password1', 'password2']


# Castom forms.

class WeatherForecastForm(forms.Form):
    """Weather forecast data form."""

    location = forms.CharField(max_length=255, help_text='Enter the location of the weather forecast', widget=forms.TextInput(attrs={'placeholder': 'location'}), error_messages={'required': 'Input location'})


class UserEditForm(UserChangeForm):
    """A form for updating users. Includes all the fields on the user, but replaces the password field with admin's password hash display field."""

    password = ReadOnlyPasswordHashField(label='password',
                                         help_text="Raw passwords are not stored, so there is no way to see this user's password",
                )

    class Meta:
        model = Users
        fields = ['username']

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        if instance:
            kwargs['initial'] = {'username': instance.username}
        super().__init__(*args, **kwargs)
