from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Organization(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'organizations'
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
