from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ["user", "profile_photo", "brief_info"]
    list_display_links = ["user", "brief_info"]

    def brief_info(self, user: Profile):
        return f"{user.user.first_name} {user.user.last_name} wrote {len(user.bio)} symbols"

    @admin.display(description='User_photo', ordering='user__date_joined')
    def profile_photo(self, user: Profile):
        return mark_safe(f"<img src='{user.user_photo.url}' width=50> ")
