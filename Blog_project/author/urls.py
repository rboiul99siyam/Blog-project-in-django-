from django.contrib import admin
from django.urls import path , include

from . import views
urlpatterns = [
    path('Register/', views.RegisterForm,name='Register'),
    path('login/', views.user_login,name='login'),
    path('logout/', views.user_logout,name='logout'),
    path('profile/', views.profile,name='profile'),
    path('update_profile/edit', views.update_profile,name='update_profile'),
    path('password_change/', views.user_pass_change,name='password_change'),
]
