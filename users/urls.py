from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('logout', views.logout, name='logout'),
]
