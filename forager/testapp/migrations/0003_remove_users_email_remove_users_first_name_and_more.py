# Generated by Django 4.2.9 on 2024-01-23 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_users_email_users_first_name_users_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='email',
        ),
        migrations.RemoveField(
            model_name='users',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='users',
            name='last_name',
        ),
    ]
