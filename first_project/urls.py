"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from first_app import views

urlpatterns = [
    path('summary/', views.summary_pg, name='summary_pg'),
    path('wd_list/', views.wd_list_pg, name='wd_list'),
    path('dp_list/', views.dp_list_pg, name='dp_list'),
    path('wd_list/search', views.SearchResultsView_wd.as_view(), name='search_wd'),
    path('dp_list/search', views.SearchResultsView_dp.as_view(), name='search_dp'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.user_login, name='login'),
    path('admin/', admin.site.urls),
    path('form/', views.dp_form, name='dp_form'),
    path('form/', include('first_app.urls')),

]
