# Generated by Django 2.2.5 on 2020-04-16 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0018_auto_20200416_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='witdrawal_form',
            name='amount',
            field=models.IntegerField(blank=True),
        ),
    ]
