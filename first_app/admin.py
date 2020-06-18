from django.contrib import admin
from .models import Witdrawal_Form, Deposit_Form, UserProfileInfo
# Register your models here.

class Wd_list_admin(admin.ModelAdmin):
    list_display = ('id', 'created_date', 'modified_date', 'company', 'name', 'bank_name', 'mail' ,'iban', 'amount', 'status',)

class Dp_list_admin(admin.ModelAdmin):
    list_display = ('id', 'created_date', 'modified_date', 'company', 'name', 'username', 'bank_name', 'amount', 'status',)


admin.site.register(Witdrawal_Form, Wd_list_admin)
admin.site.register(Deposit_Form, Dp_list_admin)
admin.site.register(UserProfileInfo)