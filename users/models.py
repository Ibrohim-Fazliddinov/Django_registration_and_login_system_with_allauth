from django.contrib.auth.models import User, AbstractUser
from django.db import models
import PIL


def user_directory_path(instance, filename):
    return f'users_{instance.user.username}/{filename}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_photo = models.ImageField(upload_to=user_directory_path, default='default.png')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
