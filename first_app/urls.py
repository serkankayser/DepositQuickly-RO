from django.urls import path
from first_app import views

urlpatterns = [
    path('selectValue/', views.sl_value, name='selectValue'),
    path('sendMoney/', views.send_money, name='sendMoney'),
]
