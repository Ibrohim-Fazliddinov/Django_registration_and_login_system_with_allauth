from django.contrib import admin
from .models import Profile
from django.utils.safestring import mark_safe


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Кастомная админка для пользователя"""
    model = Profile
    list_display = ["user", "profile_photo", "brief_info"]  # Поля, которые будут отображаться в списке объектов
    list_display_links = ["user", "brief_info"]  # Поля, которые будут ссылками на объект

    def brief_info(self, profile: Profile) -> str:
        """
        Метод для отображения краткой информации о пользователе.
        Возвращает строку с именем и количеством символов в биографии.
        """
        return f"{profile.user.first_name} {profile.user.last_name} wrote {len(profile.bio)} symbols"

    @admin.display(description='User_photo', ordering='user__date_joined')
    def profile_photo(self, profile: Profile) -> str:
        """
        Метод для отображения фото профиля в админке.
        Возвращает HTML-код для отображения изображения.
        """
        return mark_safe(f"<img src='{profile.user_photo.url}' width=50> ")

