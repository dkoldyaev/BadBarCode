__author__ = 'dkoldyaev'

from django.views.generic import CreateView, ListView, View
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from drinks.models import Drink
from persons.models import Person

class DrinkView(View) :

    def get(self, request):
        achievement = []
        person = None
        errors = []
        if request.GET.get('person_id', False) :
            try :
                person = Person.objects.get(id=request.GET.get('person_id'))
            except Person.DoesNotExist :
                raise
            new_drink = Drink()
            new_drink.person = person
            new_drink.save()
            achievement = new_drink.tryAchievement()
        return JsonResponse({
            'person':       person,
            'achievement':  achievement
        })