__author__ = 'dkoldyaev'

from django.db import models

class Person(models.Model):

    name =              models.CharField(blank=False, null=False, max_length=255, verbose_name='ФИО')
    age =               models.PositiveIntegerField(blank=False, null=False, verbose_name='Возраст')
    photo =             models.ImageField(blank=True, null=True, upload_to='persons/person/photo', verbose_name='Фоточка')
    status =            models.CharField(blank=True, null=True, max_length=255, verbose_name='Статус на ЗМШ')

    barcode =           models.ImageField(blank=True, null=False, upload_to='persons/person/barcode', verbose_name='Штрихкод')

    date_create =       models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    def tryAchievement(self):
        import random
        return random.choice([
            'Оскорбление от бармена',
            'Вставай в конец очереди',
            'Пей пиво вместо коктейля'
        ] + [None]*20)

    class Meta:
        ordering = ['name']
        verbose_name =  'Участник'
        verbose_name_plural = 'Участники'