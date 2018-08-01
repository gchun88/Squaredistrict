# Generated by Django 2.0.7 on 2018-07-31 03:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='spot_price',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bch', models.FloatField(default=None)),
                ('bth', models.FloatField(default=None)),
                ('eth', models.FloatField(default=None)),
                ('ltc', models.FloatField(default=None)),
                ('dt', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
