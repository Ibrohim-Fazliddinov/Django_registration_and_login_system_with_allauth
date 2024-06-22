from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),  # Главная страница
    path('register', views.RegisterView.as_view(), name='register'),  # Страница регистрации
    path('login/', views.CustomLoginView.as_view(), name='login'),  # Страница входа
    path('profile/', views.ProfileView.as_view(), name='profile'),  # Страница профиля
    path('logout', views.CustomLogoutView.as_view(), name='logout'),  # Страница выхода
    path('update_profile/<int:pk>/', views.UpdateProfileView.as_view(), name='update_profile'),  # Страница обновления профиля
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),  # Страница изменения пароля

    # Маршруты для сброса пароля
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='reset_password'),  # Страница запроса сброса пароля
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_sent.html'),
         name='password_reset_done'),  # Страница уведомления об отправке письма для сброса пароля
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_form.html'),
         name='password_reset_confirm'),  # Страница сброса пароля с токеном
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_complete'),  # Страница уведомления о завершении сброса пароля
]
