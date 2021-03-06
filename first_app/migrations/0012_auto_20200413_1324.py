# Generated by Django 2.2.5 on 2020-04-13 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0011_userprofileinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='witdrawal_form',
            name='bank_name',
            field=models.CharField(choices=[('Banca Transilvania', 'Banca Transilvania'), ('Bancpost', 'Bancpost'), ('BCR', 'BCR'), ('BRD', 'BRD'), ('CEC Bank', 'CEC Bank'), ('Credit Europe Bank', 'Credit Europe Bank'), ('First Bank', 'First Bank'), ('Garanti', 'Garanti'), ('ING', 'ING'), ('UniCredit Bank', 'UniCredit Bank'), ('Raiffeisen Bank', 'Raiffeisen Bank')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='witdrawal_form',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Rejected', 'Rejected')], default='Pending', max_length=15),
        ),
    ]
