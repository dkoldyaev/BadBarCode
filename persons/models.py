__author__ = 'dkoldyaev'

from django.db import models
from django import forms
from drinks.models import Drink

class Person(models.Model):

    name =              models.CharField(blank=False, null=False, max_length=255, verbose_name='ФИО')
    number =		models.CharField(blank=False, null=False, max_length=255, verbose_name='Штрихкод')
    comment =		models.CharField(blank=False, null=False, max_length=255, verbose_name='Смешной коммент')
    photo =             models.TextField(blank=True, null=True, verbose_name='Фоточка')

    date_create =       models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    

    @property
    def drinks_count(self):
        return Drink.objects.filter(person=self).count()

    def __str__(self):
        return self.name

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
