# Generated by Django 3.2.4 on 2021-06-07 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='invite_reason',
        ),
    ]
