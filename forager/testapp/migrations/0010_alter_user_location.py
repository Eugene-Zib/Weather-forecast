# Generated by Django 4.2.9 on 2024-01-25 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0009_alter_user_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(default='', max_length=255),
        ),
    ]
