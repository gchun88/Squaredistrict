# Generated by Django 2.1 on 2018-08-22 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cquser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_token',
            name='id',
        ),
        migrations.AlterField(
            model_name='user_token',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
