# Generated by Django 2.2.5 on 2020-01-12 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20200112_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='cekim_formu',
            name='status',
            field=models.CharField(default='Beklemede', max_length=20),
        ),
    ]