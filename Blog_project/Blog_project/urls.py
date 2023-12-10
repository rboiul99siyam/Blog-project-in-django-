from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='homePage'),
    path('author/', include('author.urls')),
    path('catagories/', include('catagories.urls')),
    path('posts/', include('posts.urls')),
    path('profiles/', include('profiles.urls')),
]
