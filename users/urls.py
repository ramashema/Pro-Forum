"""Urls patterns form users app"""

from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    # include default django authentication urls
    path('', include('django.contrib.auth.urls')),  # home page
    path('confirm_logout', views.confirm_logout, name='confirm_logout'), # confirm loggeout
    path('register', views.register, name='register'), # user registration
]