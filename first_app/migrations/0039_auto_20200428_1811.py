# Generated by Django 2.2.5 on 2020-04-28 18:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0038_auto_20200428_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit_form',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='witdrawal_form',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]