__author__ = 'dkoldyaev'

from django.db import models

class Drink(models.Model):

    person =        models.ForeignKey('persons.Person', blank=False, null=False,
                                      related_name='drinks')
    date =          models.DateTimeField(auto_now_add=True)

    def tryAchievement(self):
        return self.person.tryAchievement()
    
    def __str__(self):
        return '%s (%s)' % (self.person.__str__(), self.date.__str__())

    class Meta:
        verbose_name = 'Дринк'
        verbose_name_plural = 'Дринки'
