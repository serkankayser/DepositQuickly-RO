# Generated by Django 3.0.6 on 2020-06-18 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0055_paypal_deposit_form_paypal_witdrawal_form'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PayPal_Deposit_Form',
        ),
        migrations.DeleteModel(
            name='PayPal_Witdrawal_Form',
        ),
        migrations.AddField(
            model_name='witdrawal_form',
            name='mail',
            field=models.EmailField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='witdrawal_form',
            name='bank_name',
            field=models.CharField(choices=[('PayPal', 'Paypal'), ('Banca Transilvania', 'Banca Transilvania'), ('Bancpost', 'Bancpost'), ('BCR', 'BCR'), ('BRD', 'BRD'), ('CEC Bank', 'CEC Bank'), ('Credit Europe Bank', 'Credit Europe Bank'), ('First Bank', 'First Bank'), ('Garanti', 'Garanti'), ('ING', 'ING'), ('UniCredit Bank', 'UniCredit Bank'), ('Raiffeisen Bank', 'Raiffeisen Bank')], default='', max_length=50),
        ),
    ]
