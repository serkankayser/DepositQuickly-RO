# Generated by Django 3.0.6 on 2020-05-10 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0049_auto_20200429_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit_form',
            name='company',
            field=models.CharField(choices=[('xbet', 'xbet'), ('ybet', 'ybet'), ('zbet', 'zbet')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='witdrawal_form',
            name='company',
            field=models.CharField(choices=[('xbet', 'xbet'), ('ybet', 'ybet'), ('zbet', 'zbet')], default='', max_length=50),
        ),
    ]