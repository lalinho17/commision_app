# Generated by Django 5.1.4 on 2024-12-21 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fintech_app', '0003_remove_account_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='name',
        ),
    ]
