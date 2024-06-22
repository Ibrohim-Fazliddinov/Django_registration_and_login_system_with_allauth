from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Сигнал для создания или обновления профиля пользователя при сохранении объекта User.
    """
    if created:
        # Создаем профиль, если пользователь был создан
        Profile.objects.create(user=instance)
    else:
        # Сохраняем профиль, если пользователь был обновлен
        instance.profile.save()
