# Generated by Django 2.2.5 on 2020-04-28 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0044_auto_20200428_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit_form',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='witdrawal_form',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
