# Generated by Django 3.0.6 on 2020-05-10 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0053_auto_20200511_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='witdrawal_form',
            name='company',
            field=models.CharField(choices=[('xbet', 'xbet'), ('ybet', 'ybet'), ('zbet', 'zbet')], max_length=50),
        ),
    ]