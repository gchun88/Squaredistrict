# Generated by Django 2.1 on 2018-08-12 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cquser', '0003_auto_20180811_2358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactionm',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user_token',
            name='req1',
        ),
        migrations.RemoveField(
            model_name='user_token',
            name='req10',
        ),
        migrations.RemoveField(
            model_name='user_token',
            name='req10_a',
        ),
        migrations.RemoveField(
            model_name='user_token',
            name='req1_a',
        ),
        migrations.RemoveField(
            model_name='user_token',
            name='req2',
        ),
        migrations.RemoveField(
            model_name='user_token',
            name='req2_a',
        ),
        migrations.RemoveField(
            model_name='user_token',
            name='req3',
        ),
        migrations.RemoveField(
            model_name='user_token',
            name='req3_a',
        ),
        migrations.RemoveField(
            model_name='user_token',
            name='req4',
        ),
        migrations.RemoveField(
            model_name='user_token',
            name='req4_a',
        ),
        migrations.RemoveField(
            model_name='user_token',
            name='req5',
        ),
        migrations.RemoveField(
            model_name='user_token',
            name='req5_a',
        ),
        migrations.RemoveField(
            model_name='user_token',
            name='req6',
        ),
        migrations.RemoveField(
            model_name='user_token',
            name='req6_a',
        ),
        migrations.RemoveField(
            model_name='user_token',
            name='req7',
        ),
        migrations.RemoveField(
            model_name='user_token',
            name='req7_a',
        ),
        migrations.RemoveField(
            model_name='user_token',
            name='req8',
        ),
        migrations.RemoveField(
            model_name='user_token',
            name='req8_a',
        ),
        migrations.RemoveField(
            model_name='user_token',
            name='req9',
        ),
        migrations.RemoveField(
            model_name='user_token',
            name='req9_a',
        ),
        migrations.AlterField(
            model_name='transactionm',
            name='chainid',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='transactionm',
            name='transaction_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]