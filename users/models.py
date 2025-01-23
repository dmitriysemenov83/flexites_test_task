import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from organizations.models import Organization, NULLABLE
from django_resized import ResizedImageField


def user_avatar_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return f'avatars/{filename}'


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')

    first_name = models.CharField(max_length=20, **NULLABLE, verbose_name='Имя')
    last_name = models.CharField(max_length=20, **NULLABLE, verbose_name='Фамилия')
    phone = models.CharField(max_length=15, **NULLABLE, verbose_name='Телефон')
    # avatar = models.ImageField(upload_to='avatars/', **NULLABLE, verbose_name='Фотография')
    avatar = ResizedImageField(size=[200, 200], upload_to=user_avatar_path, force_format='JPEG',
                               quality=75, **NULLABLE)
    organizations = models.ManyToManyField(Organization, related_name='users', verbose_name='Организации')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'



