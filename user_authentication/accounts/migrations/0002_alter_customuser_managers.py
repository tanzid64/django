# Generated by Django 5.0.4 on 2024-04-14 06:20

import accounts.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', accounts.managers.CustomUserManager()),
            ],
        ),
    ]
