# Generated by Django 2.2.5 on 2020-01-12 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0006_auto_20200112_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Witdrawal_Form',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=264)),
                ('bank_name', models.CharField(max_length=50)),
                ('iban', models.CharField(max_length=26)),
                ('amount', models.IntegerField()),
                ('status', models.CharField(default='Pending', max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Cekim_Formu',
        ),
    ]