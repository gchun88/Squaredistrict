# Generated by Django 2.0.6 on 2018-07-22 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cquser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
