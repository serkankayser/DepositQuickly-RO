# Generated by Django 2.2.5 on 2020-04-28 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0032_deposit_form_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sum',
            fields=[
                ('sum', models.IntegerField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
