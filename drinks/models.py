__author__ = 'dkoldyaev'

from django.db import models

class Drink(models.Model):

    person =        models.ForeignKey('persons.Person', blank=False, null=False)
    date =          models.DateTimeField(auto_now_add=True)

    def tryAchievement(self):
        return self.person.tryAchievement()

    class Meta:
        verbose_name = 'Дринк'
        verbose_name_plural = 'Дринки'