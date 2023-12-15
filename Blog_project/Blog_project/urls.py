from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='homePage'),
    path('category<slug:category_slug>/', views.home,name='category_wise_post'),
    path('author/', include('author.urls')),
    path('catagories/', include('catagories.urls')),
    path('posts/', include('posts.urls')),
]
