from django import forms
from first_app.models import Deposit_Form, UserProfileInfo
from django.contrib.auth.models import User

class NewDepositForm(forms.ModelForm):
    class Meta():
        model = Deposit_Form
        fields = [
            'name',
            'username',
            'bank_name',
        ]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
