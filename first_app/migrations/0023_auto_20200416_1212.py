# Generated by Django 2.2.5 on 2020-04-16 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0022_auto_20200416_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit_form',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='witdrawal_form',
            name='amount',
            field=models.IntegerField(),
        ),
    ]