# Generated by Django 2.2.5 on 2020-04-29 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0046_auto_20200428_1847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deposit_form',
            old_name='date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='witdrawal_form',
            old_name='date',
            new_name='created_date',
        ),
        migrations.AddField(
            model_name='deposit_form',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='witdrawal_form',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]