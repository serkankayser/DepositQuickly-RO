# Generated by Django 2.2.5 on 2020-04-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0016_auto_20200416_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit_form',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
