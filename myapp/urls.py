from django.contrib import admin
from django.urls import path
from myapp import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index , name='home'),
    path('index/',views.index, name='index'),
    path('services/', views.services, name='services'),
    path('vehicle/', views.vehicle, name='vehicle'),
    path('about/', views.about, name='about'),
    path('checkfare/', views.checkfare, name='checkfare'),
    path('bookingsummary/', views.bookingsummary, name='bookingsummary'),
    path('index2', views.index2, name='index2'),
    path('blog',views.blog, name='blog'),
    #path('afterproceed/', views.afterproceed, name='afterproceed'),
    #path('forgot/', views.forgot, name='forgot'),
    path('login/',views.login,name='login'),
    path('gallery/',views.gallery, name='gallery'),
    path('logout/',views.logout,name='logout'),
    path('pay/', views.initiate_payment, name='pay'),
    path('callback/', views.callback, name='callback'),
    path('faq/', views.faq, name='faq'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('payterms/',views.payterms, name='payterms'),

    #for reset password

#password_resetview
    path('reset_password',
    auth_views.PasswordResetView.as_view(),
    name='reset_password'),

#password_reset_doneview
    path('reset_password_sent',
    auth_views.PasswordResetDoneView.as_view(template_name='templates/reset_password_sent.html'), 
    name='password_reset_done'),

#password_reset_confirmview
    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name='templates/reset_password_form.html'), 
    name='password_reset_confirm'),

#password_reset_completeview
    path('reset_password_compelete',
    auth_views.PasswordResetCompleteView.as_view(template_name='templates/reset_password_done.html'), 
    name='password_reset_complete'),
]