# Generated by Django 4.2.9 on 2024-01-25 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0010_alter_user_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
