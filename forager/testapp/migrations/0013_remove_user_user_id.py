# Generated by Django 4.2.9 on 2024-01-25 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0012_alter_user_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_id',
        ),
    ]
