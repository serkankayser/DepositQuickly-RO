# Generated by Django 2.2.5 on 2020-04-28 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0036_auto_20200428_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit_form',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='witdrawal_form',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]