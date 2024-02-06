"""This is test task."""

from django.apps import AppConfig


class TestappConfig(AppConfig):
    """Application configuration."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'testapp'
