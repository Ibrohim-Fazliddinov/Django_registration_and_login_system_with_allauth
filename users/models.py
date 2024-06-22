from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    """
    Функция для определения пути сохранения пользовательских изображений.
    """
    return f'users_{instance.user.username}/{filename}'


class Profile(models.Model):
    """
    Модель профиля пользователя, связанная с моделью User.
    """
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)  # Один к одному, удаление профиля при удалении пользователя
    user_photo = models.ImageField(upload_to=user_directory_path,
                                   default='default.png')  # Загрузка изображений в указанный путь
    bio = models.TextField()  # Поле для биографии пользователя

    def __str__(self):
        """
        Метод для отображения объекта модели в виде строки.
        """
        return self.user.username
