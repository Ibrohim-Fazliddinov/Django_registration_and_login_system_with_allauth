from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from allauth.account.signals import user_signed_up

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(user_signed_up)
def populate_user_profile(request, user, **kwargs):
    sociallogin = kwargs['sociallogin']
    if sociallogin.account.provider == 'github':  # или другой провайдер
        user.email = sociallogin.account.extra_data.get('email')
        user.save()
