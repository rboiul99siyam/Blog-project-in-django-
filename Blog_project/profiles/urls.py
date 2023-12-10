from django.contrib import admin
from django.urls import path , include

from . import views
urlpatterns = [
    path('add_profiles/', views.Add_profiles,name='add_profiles'),
]
