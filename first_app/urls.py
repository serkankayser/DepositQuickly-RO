from django.urls import path
from first_app import views

urlpatterns = [
    path('selectValue/', views.sl_value, name='selectValue'),
    path('sendMoney/', views.send_money, name='sendMoney'),
    path(r'^paydone/$', views.payment_done, name='paydone'),
    path(r'^canceled/$', views.payment_canceled, name='canceled'),
    path(r'^paypal/$', views.paypal_method, name='paypal'),
]
