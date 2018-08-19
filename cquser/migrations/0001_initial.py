# Generated by Django 2.0.7 on 2018-08-17 22:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='transactionM',
            fields=[
                ('chainid', models.IntegerField(default=1)),
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('coin', models.CharField(max_length=10)),
                ('price', models.FloatField(default=None)),
                ('coinamt', models.FloatField(default=None)),
                ('b_s', models.CharField(max_length=10)),
                ('active', models.IntegerField(default=1)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='user_token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=80)),
                ('refresh_token', models.CharField(max_length=80)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
