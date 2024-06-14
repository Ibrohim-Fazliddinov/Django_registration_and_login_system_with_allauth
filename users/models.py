from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.template.defaultfilters import slugify


def user_directory_path(instance, filename):
    return f'users_{instance.username}/{filename}'


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, null=False, blank=True)
    user_photo = models.ImageField(default='default.png', upload_to=user_directory_path)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.email

    #
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.email)

        # img = Image.open(self.user_photo.path)
        #
        # if img.height > 100 or img.width > 100:
        #     new_img = (100, 100)
        #     img.thumbnail(new_img)
        #     img.save(self.user_photo.path)

        return super().save(*args, **kwargs)