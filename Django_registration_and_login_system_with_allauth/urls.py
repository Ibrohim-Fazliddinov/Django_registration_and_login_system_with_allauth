from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Django_registration_and_login_system_with_allauth import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
