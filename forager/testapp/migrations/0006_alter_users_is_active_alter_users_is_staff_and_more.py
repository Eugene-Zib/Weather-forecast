# Generated by Django 4.2.9 on 2024-01-24 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_remove_users_user_from_users_id_user_user_from_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
