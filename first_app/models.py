from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username


class Witdrawal_Form(models.Model):

    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=264)
    all_bank_name = (
        ('Banca Transilvania', 'Banca Transilvania'),
        ('Bancpost', 'Bancpost'),
        ('BCR', 'BCR'),
        ('BRD', 'BRD'),
        ('CEC Bank', 'CEC Bank'),
        ('Credit Europe Bank', 'Credit Europe Bank'),
        ('First Bank', 'First Bank'),
        ('Garanti', 'Garanti'),
        ('ING', 'ING'),
        ('UniCredit Bank', 'UniCredit Bank'),
        ('Raiffeisen Bank', 'Raiffeisen Bank'),
    )
    bank_name = models.CharField(max_length=50, default='' ,choices=all_bank_name)
    iban = models.CharField(max_length=26)
    amount = models.IntegerField()
    all_status = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Rejected', 'Rejected'),
    )
    status = models.CharField(max_length=15, default='Pending', choices=all_status)
    date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.name

class Deposit_Form(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=264)
    username = models.CharField(max_length=264)
    all_bank_name = (
        ('Banca Transilvania', 'Banca Transilvania'),
        ('Bancpost', 'Bancpost'),
        ('BCR', 'BCR'),
        ('BRD', 'BRD'),
        ('CEC Bank', 'CEC Bank'),
        ('Credit Europe Bank', 'Credit Europe Bank'),
        ('First Bank', 'First Bank'),
        ('Garanti', 'Garanti'),
        ('ING', 'ING'),
        ('UniCredit Bank', 'UniCredit Bank'),
        ('Raiffeisen Bank', 'Raiffeisen Bank'),
    )
    bank_name = models.CharField(max_length=50, default='' ,choices=all_bank_name)
    amount = models.IntegerField(default=0)
    all_status = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Rejected', 'Rejected'),
    )
    status = models.CharField(max_length=15, default='In Progress', choices=all_status)

    date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.name