from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index , name='home'),
    path('index',views.index, name='index'),
    path('services/', views.services),
    path('vehicle/', views.vehicle, name='vehicle'),
    path('about/', views.about),
    path('checkfare/', views.checkfare, name='checkfare'),
    path('bookingsummary/', views.bookingsummary, name='bookingsummary'),
    path('index2', views.index2, name='index2'),
    path('blog',views.blog),
    path('afterproceed/', views.afterproceed, name='afterproceed'),
    path('forgot/', views.forgot, name='forgot'),
    path('login/',views.login,name='login'),
    path('gallery/',views.gallery, name='gallery'),
    path('logout/',views.logout,name='logout'),
   
]