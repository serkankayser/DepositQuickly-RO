# Generated by Django 2.2.5 on 2020-01-12 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20200112_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cekim_Formu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim_soyisim', models.CharField(max_length=264)),
                ('banka_adi', models.CharField(max_length=50)),
                ('iban', models.CharField(max_length=26)),
                ('miktar', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='webpage',
            name='topic',
        ),
        migrations.DeleteModel(
            name='AccessRecord',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.DeleteModel(
            name='Webpage',
        ),
    ]
