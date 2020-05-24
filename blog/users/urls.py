from django.contrib import admin
from django.urls import path
from . import views


app_name = 'users'


urlpatterns = [
    path('register/', views.register,name='register' ),
    path('user_login/', views.user_login,name='user_login' ),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'), 
    path('managePosts/', views.managePosts, name='manage-posts'),
    path('logout/', views.logmeout, name='log-out')
    
]
