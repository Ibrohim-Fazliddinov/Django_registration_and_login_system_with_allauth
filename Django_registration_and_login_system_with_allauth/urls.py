from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include


def home(request):
    return render(request, 'base.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('allauth.urls')),
    path('', home),
]
