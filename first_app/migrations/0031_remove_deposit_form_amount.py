# Generated by Django 2.2.5 on 2020-04-16 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0030_auto_20200416_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deposit_form',
            name='amount',
        ),
    ]
