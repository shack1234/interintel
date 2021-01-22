 
from django.urls import path, include
#from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers
from .views import *
from .views import ChangePasswordView
urlpatterns = [
    path('',views.indexPage, name='index'),
    path('account/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('profile/<username>/', views.profile, name='profile'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="registration/forgot-password.html"),name="reset_password"),
]

