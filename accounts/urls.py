from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from .views import *

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login_view_url'),
    path('registration/', RegistrationPageView.as_view(), name='registration_view_url'),
    path('logout/', LogoutView.as_view(), name='logout_view_url'),
    path('profile/', ProfileView.as_view(), name='profile_view_url'),
    # path('password-change/', ProfilePasswordChangeView.as_view(), name='password_change_view_url'),
    # path('username_change/', ProfileUsernameChangeView.as_view(), name='username_change_view_url'),
]
