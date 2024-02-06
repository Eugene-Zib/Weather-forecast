# Generated by Django 4.2.9 on 2024-01-23 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_rename_user_from_users_users_user_from_users_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='user_from_users_id',
        ),
        migrations.AddField(
            model_name='user',
            name='user_from_users',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='testapp.users'),
        ),
    ]