# Generated by Django 4.2.9 on 2024-01-30 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0013_remove_user_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='forecast',
            field=models.CharField(default='sun', max_length=50),
        ),
    ]
