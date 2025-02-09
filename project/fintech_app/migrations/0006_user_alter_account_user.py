# Generated by Django 5.1.4 on 2024-12-21 04:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fintech_app', '0005_account_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=254, unique=True)),
                ('Id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='user',
            field=models.ForeignKey(default='User', on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='fintech_app.user'),
        ),
    ]
